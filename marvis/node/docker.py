"""Docker containers in the simulation."""

import logging
import os
import threading

from nsenter import Namespace
import docker

from ..context import defer
from ..command_executor import DockerCommandExecutor
from .base import Node

logger = logging.getLogger(__name__)

def expand_volume_shorthand(key_value):
    """Expand a volume string to something the Docker runtime understands.

    Parameters
    ----------
    key_value : str or dict
        The volume configuration

    Returns
    -------
    tuple
        Return the volume's name / path and a settings dictionary.
    """
    name_or_path, spec = key_value
    if isinstance(spec, str):
        return (name_or_path, {'bind': spec, 'mode': 'rw'})
    return (name_or_path, spec)

def log_to_file(container, log_path, stdout=False, stderr=False):
    """Log the container's output.

    This opens a stream to the docker container's log output and writes it into a file.

    Parameters
    ---------
    log_path : str
        The file path to the log file.
    stdout : bool
        Whether stdout should be logged.
    stderr : bool
        Whether stderr should be logged.
    """
    log = logging.getLogger(container.name)
    log.debug('Write log to %s', log_path)
    with open(log_path, 'wb', 0) as log_file:
        for line in container.logs(stdout=stdout, stderr=stderr, follow=True, stream=True):
            log.log(logging.INFO if stdout else logging.ERROR, '%s', line.decode().strip())
            log_file.write(line)
        log.debug('Done logging')

class DockerNode(Node):
    """A DockerNode represents a docker container.

    Parameters
    ----------
    name : str
        The name of the node (and container).
        It must consist only of *alphanumeric characters* and :code:`-`, :code:`_` and :code:`.`.
    docker_image : str
        The name of the docker image to use. If not specified,
        `docker_file` and `docker_build_dir` must be set.
    docker_build_dir : str
        The context directory (relative path possible) to execute the build in.
    docker_file : str
        The (absolute or relative) path to the Dockerfile.
    pull: bool
        Whether to always pull the image specified in `docker_image`.
    cpus : float
        The number of virtual CPUs to assign (1.0 meaning 1 vCPU).
    memory : str
        The amount of memmory to allow the container to use. **Example:** `'128m'`.
    command : str
        An optional command to override the standard command on container
        start specified by the Dockerfile.
    volumes : list of dict or list of str
        A dictionary of volumes. Each entry has a name or (absolute) path as key
        and settings or a absolute path inside the container as value. See :code:`examples/volumes_and_ports.py`.
    exposed_ports : dict
        A dictionary of port mappings. The key is the container internal port and the value can
        be an exposed port or a list of ports.
    environment_variables : dict or list
        A dictonary of environment variables or a list of environment variables.
        If a list is specified each item should be in the form :code:`'KEY=VALUE'`.
    """

    def __init__(self, name, docker_image=None, docker_build_dir=None, dockerfile='Dockerfile', pull=False,
                 cpus=0.0, memory=None, command=None, volumes=None, exposed_ports=None, environment_variables=None):
        super().__init__(name)
        #: The docker image to use.
        self.docker_image = docker_image
        #: The context to build the image in.
        self.docker_build_dir = docker_build_dir
        #: The path to the Dockerfile.
        self.dockerfile = dockerfile
        #: Enforce pulling the image from a registry
        self.pull = pull

        #: The number of vCPUs.
        self.cpus = cpus
        #: The amount of memory for the container.
        self.memory = memory

        #: The startup command.
        self.command = command
        #: The volumes for the container.
        self.volumes = dict(map(expand_volume_shorthand, volumes.items())) if volumes else None
        #: Ports to expose on the host.
        self.exposed_ports = exposed_ports if exposed_ports is not None else dict()
        #: Environment variables in the container.
        self.environment_variables = environment_variables

        #: The container instance.
        self.container = None
        #: The PID of the container.
        self.container_pid = None

        if docker_build_dir is None and docker_image is None:
            raise Exception('Please specify Docker image or build directory')

        #: The executor for running commands in the container.
        #: This is useful for a scripted :class:`.Workflow`.
        self.command_executor = None

    @property
    def docker_image_tag(self):
        """A tag for the container's image during build time.

        Returns
        -------
        str
            The computed tag.
        """
        return f'ns3-{self.name}'

    def wants_ip_stack(self):
        return True

    def prepare(self, simulation):
        """This runs a setup on network interfaces and starts the container."""
        logger.info('Preparing node %s', self.name)
        self.build_docker_image()
        self.start_docker_container(simulation.log_directory, simulation.hosts)
        self.setup_host_interfaces()

    def build_docker_image(self):
        """Build the image for the container."""
        client = docker.from_env()
        if self.docker_image is None:
            logger.info('Building docker image: %s/%s', self.docker_build_dir, self.dockerfile)
            self.docker_image = client.images.build(
                path=self.docker_build_dir,
                dockerfile=self.dockerfile,
                rm=True,
                nocache=False,
            )[0]
        elif isinstance(self.docker_image, str):
            if not self.pull:
                try:
                    self.docker_image = client.images.get(self.docker_image)
                except docker.errors.ImageNotFound:
                    pass

            if isinstance(self.docker_image, str):
                repo, *tag = self.docker_image.split(':')
                tag = tag[0] if not tag else 'latest'
                logger.info('Pulling docker image: %s, tag %s', repo, tag)
                self.docker_image = client.images.pull(repo, tag=tag)

        self.docker_image.tag(self.docker_image_tag)

    def start_docker_container(self, log_directory, hosts=None):
        """Start the docker container.

        All docker containers are labeled with "ns-3" as the creator.

        Parameters
        ----------
        log_directory : str
            The path to the directory to put log files in.
        hosts : dict
            A dictionary with hostnames as keys and IP addresses (a list) as value.
        """
        logger.info('Starting docker container: %s', self.name)
        client = docker.from_env()

        extra_hosts = [f'{name}:{address}' for name, addresses in hosts.items() for address in addresses]

        self.container = client.containers.run(
            self.docker_image_tag,
            name=self.name,
            hostname=self.name,
            labels={"created-by": "ns-3"},

            remove=True,
            auto_remove=True,
            detach=True,

            privileged=True,
            nano_cpus=int(self.cpus * 1e9),
            mem_limit=0 if self.memory is None else self.memory,

            command=self.command,
            extra_hosts=extra_hosts,
            volumes=self.volumes,
            ports=self.exposed_ports,
            environment=self.environment_variables,
        )
        defer(f'stop docker container {self.name}', self.stop_docker_container)

        for stream in ('stdout', 'stderr'):
            log_file_path = os.path.join(log_directory, f'{self.name}.{stream}.log')
            threading.Thread(target=log_to_file, args=(self.container, log_file_path), kwargs={stream: True}).start()

        low_level_client = docker.APIClient()
        self.container_pid = low_level_client.inspect_container(self.container.id)['State']['Pid']

        self.command_executor = DockerCommandExecutor(self.name, self.container)

    def stop_docker_container(self):
        """Stop the container."""
        if self.container is not None:
            logger.info('Stopping docker container: %s', self.container.name)
            self.container.stop(timeout=1)
            self.container = None
            self.container_pid = None
            self.command_executor = None

    def setup_host_interfaces(self):
        """Setup the interfaces (bridge, tap, VETH pair) on the host and connect
            them to the container."""
        for name, interface in self.interfaces.items():
            interface.setup_bridge()
            interface.connect_tap_to_bridge()
            interface.setup_veth_pair({
                'ifname': name,
                "net_ns_fd": f"/proc/{self.container_pid}/ns/net"
            })

            # Get container's namespace and setup the interface in the container
            with Namespace(self.container_pid, 'net'):
                interface.setup_veth_container_end(name)
