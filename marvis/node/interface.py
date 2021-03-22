
import logging
from pyroute2 import IPRoute

from ..command_executor import ConsoleCommandExecutor
from .base import Node

logger = logging.getLogger(__name__)


class InterfaceNode(Node):
	"""A Interface Node represents a node (or network) behind an local network interface.
	This is an easy and simple way to include external nodes inside of the simulation.

	Parameters
	----------
	name : str
		The name of the node.
		It must consist only of *alphanumeric characters* and :code:`-`, :code:`_` and :code:`.`.
	ifname : str
		The name of the local network interface. Default is eth0.
	"""

	def __init__(self, name, ifname='eth0'):
		super().__init__(name)

		#: The interface name on the local machine.
		self.ifname = ifname

		#: The executor for running commands on the external device.
		#: This is useful for a scripted :class:`Workflow`.
		self.command_executor = ConsoleCommandExecutor(self.name)

	def wants_ip_stack(self):
		return False

	def prepare(self, simulation):
		"""This creates the bridge and connects the local NIC to the bridge.
		"""
		ipr = IPRoute()
		for interface in self.interfaces.values():
			interface.setup_bridge()
			interface.connect_tap_to_bridge(tap_mode="UseLocal")
			ipr.link('set', ifname=self.ifname, master=ipr.link_lookup(ifname=interface.bridge_name)[0])
