"""QEMU VM in the simulation."""

import logging
import os
import threading
import time
import paramiko

from ..context import defer
from ..command_executor import LocalCommandExecutor, SSHCommandExecutor
from .base import Node

logger = logging.getLogger(__name__)

class QEMUNode(Node):
    """A QEMUNode represents a QEMU VM.

    Parameters
    ----------
    name : str
        The name of the node (and QEMU instance).
        It must consist only of *alphanumeric characters* and :code:`-`, :code:`_` and :code:`.`.
    ip : str
        The ip address for the connection to the QEMU VM.
        Must be unique and not in use already. Cohydra will set it up automatically.
        Format is `a.b.c.d`, where `d` not equal 1.
    image_path : str
        The (absolute or relative) path to the QEMU image file.
    username : str
        The username for the QEMU vm.
    system: str
        The system to start QEMU with. **Example:** `'qemu-system-x86_64'`
    qemu_options : str
        Additional QEMU starting parameters.
    mac_address : str
        The mac address of the QEMU VMs main network interface (guest_interface) will be set to the entered value.
    guest_interface : str
        Name of the guests main network interface for communication with the host.
    copy_vm : bool
        If set to :code:`True` the QEMU image will be copied and this copy will be deleted afterwards.
        Currently not implemented!
    """

    def __init__(self, name, ip=None, image_path=None, username=None, password=None, system=None, qemu_options="", mac_address=None, guest_interface=None, copy_vm=True):
        super().__init__(name)

        #: The ip of the VM's interface to communicate with the host and allow access via ssh.
        self.ip = ip
        #: The QEMU image to use.
        self.image_path = image_path
        #: The username.
        self.username = username
        #: The password.
        self.password = password
        #: The interface on the virtual machine for communication with the host.
        self.guest_interface = guest_interface

        #: QEMU system to use for this image, ex: qemu-system-x86_64, qemu-system-arm, ...
        self.system = system

        #: PID of the QEMU instance. Required to terminate process afterwards.
        self.proc_id = None

        #: MAC address must be specified by the user to successfully add the device to Cohydras ns-3 network.
        self.mac_address = mac_address
        if mac_address is None:
            raise Exception('Please specify the mac_address: xx:xx:xx:xx:xx:xx')

        #: Additional QEMU options.
        self.qemu_options = f'-hda {self.image_path} {qemu_options} -no-reboot -daemonize -display none -net nic,macaddr={mac_address} -net tap'

        if image_path is None or system is None or guest_interface is None:
            raise Exception('Please specify image path, system and guest_interfaces')

        #: For commands executed on the host machine.
        self.local_command_executor = LocalCommandExecutor(self.name)

        #: For commands executed on the QEMU VM.
        self.command_executor = None

    def wants_ip_stack(self):
        return True

    def prepare(self, simulation):
        """This runs a setup on network interfaces and starts the QEMU VM."""
        logger.info('Preparing node %s', self.name)
        self.setup_host_interfaces()
        self.start_qemu()
        success = self.wait_for_connection()
        if(success):
            for interface in self.interfaces.values():
                self.setup_remote_address(interface.address)

    def copy_qemu_image(self):
        # TODO
        pass

    def setup_host_interfaces(self):
        """Setup the interfaces (bridge, tap and IP on device) on the host and guest machine.
        Generates management IP from given guest machine IP.
        """
        host_ip = self.ip[0:self.ip.rfind('.')] + '.1'
        for name, interface in self.interfaces.items():
            interface.setup_bridge()
            interface.connect_tap_to_bridge()
        for interface in self.interfaces.values():
            interface.setup_qemu_host_address(host_ip)

    def start_qemu(self):
        """Start the QEMU VM with the additional parameters set by the user.
        Creates an additional tap device for the communication with the host machine.
        Enables proxy_arp and sets the local command executor up (commands on host side)
        """
        logger.info('Starting QEMU instance: %s', self.name)
        tap_name = f'{self.name}-tap'

        self.local_command_executor.execute(f'{self.system} {self.qemu_options},ifname={tap_name}', shell=True)
        self.proc_id = self.get_pid('qemu', f'ifname={tap_name}')
        for interface in self.interfaces.values():
            self.local_command_executor.execute(f'ip link set {tap_name} master {interface.bridge_name}', shell=True)
        #self.local_command_executor.execute(f'echo 1 > /proc/sys/net/ipv4/conf/{self.host_interface}/proxy_arp', shell=True)
        self.local_command_executor.execute(f'echo 1 > /proc/sys/net/ipv4/conf/{tap_name}/proxy_arp', shell=True)
        defer(f'stop QEMU instance {self.name}', self.stop_qemu_vm)

        self.local_command_executor = LocalCommandExecutor(self.name)

    def stop_qemu_vm(self):
        """Stop the QEMU VM."""
        #self.local_command_executor.execute(f'echo 0 > /proc/sys/net/ipv4/conf/{self.host_interface}/proxy_arp', shell=True)
        if(self.proc_id != -1):
            logger.info('Stopping QEMU vm: %s, with pid: %s', self.name, self.proc_id)
            self.local_command_executor.execute(f'kill -9 {self.proc_id}', shell=True)
        else:
            logger.info('Could not retrieve pid from QEMU VM: %s. To terminate all running QEMU instances do: sudo pkill qemu', self.name)

    def wait_for_connection(self):
        """Wait until the VM can be reached via SSH. Outputs logger info on timeout."""
        timeout = 0
        timeout_max = 12
        timeout_sleep = 5
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        logger.info('Waiting ' + str(timeout_max*timeout_sleep) + ' seconds for QEMU VM %s to complete booting...', self.name)
        while True:
            try:
                client.connect(self.ip, username=self.username, password=self.password)
                self.command_executor = SSHCommandExecutor(self.name, client, sudo=True)
                logger.info('ssh connection to %s successful.', self.ip)
                return True
            except Exception as ex:
                #logger.info(ex)
                if timeout > timeout_max:
                    logger.info("QEMU VM %s could not be reached.", self.name)
                    return False
                time.sleep(timeout_sleep)
                timeout += 1

    def get_custom_mac(self):
        """Returns the custom MAC address."""
        return self.mac_address

    def get_pid(self, grep, args):
        """Returns the process id of a given process with the name `grep` and the specific arguments `args`
        Required for terminating the process afterwards.

        Parameters
        ----------
        grep : str
            The name of the process
        args : str
            Additional grep parameter if more than one process with the given name (grep) exists
        """
        qemu_pids = ""
        try:
            if args != "":
                qemu_pids = self.local_command_executor.execute('pgrep ' + grep + ' -a | grep ' + args, shell=True, universal_newlines=True)
            else:
                qemu_pids = self.local_command_executor.execute('pgrep ' + grep + ' -a', shell=True, universal_newlines=True)
            pids = str(qemu_pids[:-2]).split('\n')
            for pid in pids:
                return int(pid.lstrip().split(' ')[0])
        except Exception as ex:
            logger.info('No processes %s running to retrieve pid', args)
            #logger.info(ex)
            return -1

    def setup_remote_address(self, address):
        """Add the simulation IP address to the remote device.

        Parameters
        ----------
        address : str
            The address to assign to the external node in simulation.
        """
        self.command_executor.execute(f'sudo ip addr add {address} dev {self.guest_interface}', user='root')
        defer(f'remove remote ip {address}', self.remove_remote_address, address)

    def remove_remote_address(self, address):
        """Remove the simulation IP address from the remote device.

        Parameters
        ----------
        address : str
            The address to remove from the external node.
        """
        self.command_executor.execute(f'sudo ip addr del {address} dev {self.guest_interface}', user='root')