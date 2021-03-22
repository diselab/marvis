"""LXD containers in the simulation."""

import logging

from nsenter import Namespace
import pylxd

from ..context import defer
from ..command_executor import LXDCommandExecutor
from .base import Node

logger = logging.getLogger(__name__)

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

class LXDNode(Node):
    """A LXDNode represents a LXD container.

    Parameters
    ----------
    name : str
        The name of the node (and container).
    image : str
        The name of the image to use (=the **alias**).
    image_server : str
        The server to pull the image off if not found locally.
    custom_configuration : dict
        Additional configuration key-value-pairs to pass to LXD.
    """

    def __init__(self, name, image=None, image_server='https://images.linuxcontainers.org',
                 custom_configuration=None):
        super().__init__(name)

        #: The image's name being used.
        self.image = image

        #: The container instance.
        self.container = None

        #: Custom configuration values.
        self.custom_configuration = custom_configuration

        #: The executor for running commands in the container.
        #: This is useful for a scripted :class:`.Workflow`.
        self.command_executor = None

        #: The server to fetch the image from.
        #: Before fetching from the server, local images will be checked.
        self.image_server = image_server

    def wants_ip_stack(self):
        return True

    def prepare(self, simulation):
        """This runs a setup on network interfaces and starts the container."""
        logger.info('Preparing node %s', self.name)
        self.create_container()
        self.start_container(simulation.log_directory, simulation.hosts)
        self.setup_host_interfaces()

    def create_container(self):
        """Create the LXC container."""
        logger.info('Creating LXC container for: %s', self.name)
        client = pylxd.Client()

        config = {
            'name': self.name,
            'source': {
                'type': 'image',
                'alias': self.image,
            }
        }

        if isinstance(self.custom_configuration, dict):
            config.update(self.custom_configuration)

        # Check whether image with alias exists locally.
        try:
            client.images.get_by_alias(self.image)
        except pylxd.exceptions.NotFound:
            # Not found, so use the server.
            logger.debug('Image "%s" not found locally, pulling from %s', self.image, self.image_server)
            config['source'].update({
                'protocol': 'simplestreams',
                'server': self.image_server
            })

        # Tag for removal with cleanup.
        self.container = client.containers.create(config, wait=True)
        self.container.config.update({
            'user.created-by': 'ns-3'
        })
        self.container.save(wait=True)

    def start_container(self, log_directory, hosts=None):
        """Start the LXC container.

        All docker containers are labeled with "ns-3" as the creator.

        Parameters
        ----------
        log_directory : str
            The path to the directory to put log files in.
        hosts : dict
            A dictionary with hostnames as keys and IP addresses (a list) as value.
        """
        logger.info('Starting LXC container: %s', self.name)

        defer(f'stop and delete LXD container {self.name}', self.delete_container)
        self.container.start(wait=True)

        # Add extra_hosts to hosts file.
        hosts_file_content = self.container.files.get('/etc/hosts').decode()
        extra_hosts = '\n'.join(f'{address}\t{name}' for name, addresses in hosts.items() for address in addresses)
        self.container.files.put('/etc/hosts', f'{hosts_file_content}\n{extra_hosts}\n'.encode())

        self.command_executor = LXDCommandExecutor(self.name, self.container)

    def delete_container(self):
        """Delete the container."""
        if self.container is not None:
            logger.info('Stopping LXD container: %s', self.container.name)
            self.container.stop(timeout=-1, wait=True)
            self.container.delete(wait=True)
            self.container = None
            self.command_executor = None

    def setup_host_interfaces(self):
        """Setup the interfaces (bridge, tap, VETH pair) on the host and connect
            them to the container."""
        for name, interface in self.interfaces.items():
            logger.debug('Setting up interface %s on %s.', name, self.name)
            interface.setup_bridge()
            interface.connect_tap_to_bridge()

            self.container.devices.update({
                name: {
                    'name': name,
                    'type': 'nic',
                    'nictype': 'bridged',
                    'parent': interface.bridge_name,
                    'hwaddr': interface.mac_address,
                    'host_name': interface.veth_name,
                }
            })
            self.container.save(wait=True)
            container_state = pylxd.Client().api.containers[self.name].state.get().json()
            pid = container_state['metadata']['pid']

            # Get container's namespace and setup the interface in the container
            with Namespace(pid, 'net'):
                interface.setup_veth_container_end(name)
