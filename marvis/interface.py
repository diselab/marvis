"""Internal network card."""
import logging
from pyroute2 import IPRoute
from ns import core, tap_bridge, network as ns_net
from .context import defer

logger = logging.getLogger(__name__)

class Interface:
    """The Interface resembles a network card.

    *Warning:* The interface is controlled by the a :class:`.Channel`. Do not instantiate
    an Interface by yourself.

    Parameters
    ----------
    node : :class:`.Node`
        The node to connect the interface to.
    ns3_device
        The ns-3 equivalent of the interface.
    address : str
        An IP address.
    mac_address : str
        An MAC address. If :code:`None`, a random MAC address will be assigned internally.
        **Warning:** You may need to set the MAC address in order to reach your nodes correctly.
        If you have any constraints on MAC addresses used externally, set it here.
    """
    __counter = 0

    def __init__(self, node, ns3_device, address, mac_address=None):
        #: A unique number identifying the interface.
        self.number = Interface.__counter
        Interface.__counter += 1

        #: The node to connect the interface to.
        self.node = node
        #: The ns-3 equivalent of the interface.
        self.ns3_device = ns3_device
        #: The interface's IP
        self.address = address
        #: The name of the interface. This will be set by in :func:`.Node.add_interface()`.
        self.ifname = None
        #: The MAC address of this interface.
        self.mac_address = mac_address
        if self.mac_address is None:
            allocated_mac = ns_net.Mac48Address.Allocate()
            checker = ns_net.MakeMac48AddressChecker()
            self.mac_address = ns_net.Mac48AddressValue(allocated_mac).SerializeToString(checker)

    def __interface_name(self, prefix):
        """Return the name of the interface.

        Parameters
        ----------
        prefix : str
            A prefix to the name.

        Returns
        -------
        str
            An interface name.
        """
        return f'{prefix}-ns3-{self.number}'

    @property
    def bridge_name(self):
        """Return a unique name for a bridge.

        Returns
        -------
        str
            A bridge name.
        """
        return self.__interface_name('br')

    @property
    def tap_name(self):
        """Return a unqiue name for a tap.

        Returns
        -------
        str
            A tap name.
        """
        return self.__interface_name('tap')

    @property
    def veth_name(self):
        """Return a unique name for an VETH pair.

        Returns
        -------
        str
            A VETH name.
        """
        return self.__interface_name('veth')

    @property
    def pcap_file_name(self):
        """Return the name for the PCAP log file.

        Returns
        -------
        str
            A PCAP log file name.
        """
        return f'{self.node.name}.{self.ifname}.pcap'

    def setup_bridge(self):
        """Setup a bridge for adding a tap later on."""
        ipr = IPRoute()

        logger.debug('Create bridge %s', self.bridge_name)
        ipr.link('add', ifname=self.bridge_name, kind='bridge')
        defer(f'remove bridge {self.bridge_name}', self.remove_bridge)

        ipr.link('set', ifname=self.bridge_name, state='up')

    def remove_bridge(self):
        """Destroy the bridge."""
        ipr = IPRoute()

        logger.debug('Remove bridge %s', self.bridge_name)
        ipr.link('del', ifname=self.bridge_name)

    def connect_tap_to_bridge(self, bridge_name=None, tap_mode="ConfigureLocal"):
        """Connect a ns-3 tap device to the bridge.

        Parameters
        ----------
        bridge_name : str
            The bridge to connect the tap (and ns-3) device to.
        tap_mode : str
            The ns-3 mode for the tap bridge. Either ConfigureLocal or UseLocal.
        """
        if bridge_name is None:
            bridge_name = self.bridge_name

        ipr = IPRoute()

        logger.debug('Connect %s to bridge %s via %s', self.node.name, bridge_name, self.tap_name)
        ipr.link('add', ifname=self.tap_name, kind='tuntap', mode='tap')
        defer(f'disconnect ns3 node {self.node.name}', self.disconnect_tap_from_bridge)

        ipr.link('set', ifname=self.tap_name, state='up')

        ipr.link('set', ifname=self.tap_name, master=ipr.link_lookup(ifname=bridge_name)[0])

        logger.debug("Adding TapBridge for %s.", self.node.name)
        tap_helper = tap_bridge.TapBridgeHelper()
        # ConfigureLocal is used to prevent the TAP / bridged device to use a "learned" MAC address.
        # So, we can set the CSMA and WiFiNetDevice address to something we control.
        # Otherwise, WiFi ACK misses happen.
        if tap_mode == "ConfigureLocal":
            tap_helper.SetAttribute('Mode', core.StringValue('ConfigureLocal'))
            tap_helper.SetAttribute('DeviceName', core.StringValue(self.tap_name))
            tap_helper.SetAttribute('MacAddress', ns_net.Mac48AddressValue(ns_net.Mac48Address.Allocate()))
            tap_helper.Install(self.node.ns3_node, self.ns3_device)
        elif tap_mode == "UseLocal":
            tap_helper.SetAttribute("Mode", core.StringValue("UseLocal"))
            tap_helper.SetAttribute("DeviceName", core.StringValue(self.tap_name))
            tap_helper.Install(self.node.ns3_node, self.ns3_device)
        else:
            logger.error("Unsupported TAP-Mode %s.", tap_mode)


    def disconnect_tap_from_bridge(self):
        """Disconnect the (tap) interface and delete it."""
        ipr = IPRoute()

        logger.debug('Disconnect %s from bridge via %s', self.node.name, self.tap_name)
        ipr.link('del', ifname=self.tap_name)

    def setup_veth_pair(self, peer):
        """Setup a VETH pair for containers.

        This function also connects the external site of the pair to the bridge.

        Parameters
        ----------
        peer : dict
            Options for the internal side of the VETH pair.
            This can e.g. contain the network namespace (see :class:`.DockerNode` for example).
        """
        ipr = IPRoute()

        logger.debug('Create veth pair %s on bridge %s', self.veth_name, self.bridge_name)
        peer['address'] = self.mac_address
        ipr.link('add', ifname=self.veth_name, peer=peer, kind='veth')
        defer(f'disconnect veth for ns3 node {self.node.name}', self.remove_veth_pair)
        ipr.link('set', ifname=self.veth_name, master=ipr.link_lookup(ifname=self.bridge_name)[0])
        ipr.link('set', ifname=self.veth_name, state='up')

    def remove_veth_pair(self):
        """Disconnect the veth pair and delete it."""
        ipr = IPRoute()

        logger.debug('Disconnect %s from veth via %s', self.node.name, self.veth_name)
        ipr.link('del', ifname=self.veth_name)

    def setup_veth_container_end(self, ifname):
        """Setup the VETH in a container.

        Parameters
        ----------
        ifname : str
            The interface name within the container.
        """
        ipr = IPRoute()

        logger.debug('Bind veth %s to %s at %s', self.veth_name, ifname, self.address)
        index = ipr.link_lookup(ifname=ifname)[0]
        ipr.addr('add', index=index, address=str(self.address.ip), mask=self.address.network.prefixlen)
        ipr.link('set', index=index, state='up')
