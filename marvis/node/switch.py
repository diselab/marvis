"""Simulated network switch."""

import logging

from ns import bridge, network

from .base import Node

logger = logging.getLogger(__name__)

class SwitchNode(Node):
    """This is representing a switch between other nodes.

    It uses ns-3 internals for routing.
    """

    def __init__(self, name):
        super().__init__(name)
        bridge_helper = bridge.BridgeHelper()
        #: The ns-3 internal device to route packages.
        self.bridge_device = bridge_helper.Install(self.name, network.NetDeviceContainer()).Get(0)

    def add_interface(self, interface, *args, **kwargs):  # pylint: disable=signature-differs
        assert interface.address is None, 'Bridges may not have IP addresses.'
        super().add_interface(interface, *args, **kwargs)
        self.bridge_device.AddBridgePort(interface.ns3_device)

    def prepare(self, simulation):
        pass

    def wants_ip_stack(self):
        return False

    def execute_command(self, command, user=None):
        logger.warning('Can not execute command "%s" on bridge node %s', command, self.name)
