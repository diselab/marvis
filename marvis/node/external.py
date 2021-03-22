"""Physical Nodes that are connected to the simulation host."""

import logging

from ..context import defer
from ..command_executor import ConsoleCommandExecutor
from .base import Node

logger = logging.getLogger(__name__)

class ExternalNode(Node):
    """An ExternalNode represents an external device.

    To use this kind of node you need to setup the network before.
    This includes setting up network bridges that route packages to the
    real hardware / external devices.
    Please consider the :code:`setup-external.py` script.

    Parameters
    ----------
    bridge : str
        The name of the bridge (that alread exists) to connect the simulation node to.
        If not specified, :code:`ns3-{name}` is used.
    ifname : str
        The name of the interface **on the remote device**.
    """

    def __init__(self, name, bridge=None, ifname='eth0'):
        super().__init__(name)

        if bridge is None:
            bridge = f'ns3-{name}'
        #: The name of the bridge the external node is connected to.
        self.bridge = bridge
        #: The interface name on the remote device.
        self.ifname = ifname

        #: The executor for running commands on the external device.
        #: This is useful for a scripted :class:`Workflow`.
        self.command_executor = ConsoleCommandExecutor(self.name)

    def wants_ip_stack(self):
        return False

    def prepare(self, simulation):
        """This also runs setup on the remote device by setting the IP address
        the device is assigned during simulation.
        """
        for interface in self.interfaces.values():
            interface.connect_tap_to_bridge(bridge_name=self.bridge)
            self.setup_remote_address(interface.address)

    def setup_remote_address(self, address):
        """Add the simulation IP address to the remote device.

        Parameters
        ----------
        address : str
            The address to assign to the external node in simulation.
        """
        self.execute_command(['ip', 'addr', 'add', str(address), 'dev', self.ifname], user='root')
        defer(f'remove remote ip {address}', self.remove_remote_address, address)

    def remove_remote_address(self, address):
        """Remove the simulation IP address from the remote device.

        Parameters
        ----------
        address : str
            The address to remove from the external node.
        """
        self.execute_command(['ip', 'addr', 'del', str(address), 'dev', self.ifname], user='root')
