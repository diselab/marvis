"""A subnet."""

import logging
import ipaddress
import string
import random

from .channel import CSMAChannel
from .util import network_color_for
from .node import SwitchNode

logger = logging.getLogger(__name__)

DEFAULT_PREFIX = {
    4: 24,
    6: 64,
}


class Network:
    """A network connects many nodes together and assigns IP addresses.

    It can be compared to a subnet or so.
    It should also support IPv6 (untested!).

    Parameters
    ----------
    network_address : str
        The network base address (and optional subnet mask).
        An example for this parameter could be :code:`"10.42.42.0/24"`.
    netmask : str
        The networks subnet mask. It can be used to provide a mask
        if not already given in the :code:`network_address` parameter.
    base : str
        The base / start for the IP-addresses of this network.
        An IPv4 example for this parameter could be :code:`"0.0.0.50"`.
    default_channel_type : class
        The default channel to use.
        This can be one of :class:`.CSMAChannel` or :class:`.WiFiChannel`.
    """

    def __init__(self, network_address, netmask=None, base=None, default_channel_type=CSMAChannel):
        #: All the channels in the network.
        self.channels = list()
        #: The prototypes for the future channels.
        self.channels_prototypes = list()
        #: The channel type
        self.default_channel_type = default_channel_type
        #: The list of random generated channel names to avoid duplicates
        self.random_channel_names = set()
        #: The list of the connected nodes
        self.nodes = list()
        #: The list of already allocated ip addresses
        self.allocated_ip_addresses = list()

        if isinstance(network_address, str):
            if '/' in network_address:
                network_address = ipaddress.ip_network(network_address)
            else:
                if netmask is None:
                    netmask = DEFAULT_PREFIX[ipaddress.ip_address(network_address).version]
                network_address = ipaddress.ip_network(f'{network_address}/{netmask}')
        #: The network's address (containing the subnet mask).
        self.network = network_address
        #: The network's netmask
        self.netmask = netmask
        #: The next potentially free ip address of that network moved by base
        self.next_free_ip = None
        if base is None:
            self.next_free_ip = ipaddress.ip_address(self.network.network_address) + 1
        else:
            self.next_free_ip = ipaddress.ip_address(self.network.network_address) + int(ipaddress.ip_address(base))
        #: The color of the network's nodes in a visualization.
        self.color = None

    def create_channel(self, name=None, channel_type=None, **channel_kwargs):
        """Adds one named channel prototype to the network.

        Parameters
        ----------
        name : str
            The name of the channel. If set to :code:`None`, a random name will be generated
        channel_type : class
            The channel type. If set to :code:`None`, the default channel type will be set.
        channel_kwargs : dict
            The arguments of the new channel
        """
        if name is None:
            letters = string.ascii_lowercase
            name = "channel_" + "".join(random.choice(letters) for i in range(4))
            while name in self.random_channel_names:
                name = "channel_" + "".join(random.choice(letters) for i in range(4))
            self.random_channel_names.add(name)

        if channel_type is None:
            channel_type = self.default_channel_type

        prototype = ChannelPrototype(self, name, channel_type, channel_kwargs)
        self.channels_prototypes.append(prototype)
        return prototype

    def block_ip_address(self, ip_addr):
        """Blocks an IP address.

        That IP address will not be assigned to any node.

        Parameters
        ----------
        ip_addr : str
            The IP address which will be blocked.
        """
        logger.info('Block the IP address %s in the network %s/%s', ip_addr, self.network, self.netmask)
        address = ipaddress.ip_address(ip_addr)
        if address in self.allocated_ip_addresses:
            raise ValueError(f'IP address {ip_addr} already in use')
        self.allocated_ip_addresses.append(address)

    def get_free_ip_address(self):
        """Get a free ip address.

        This returns an ip address which is not already allocated or blocked.
        """
        address = self.next_free_ip
        self.next_free_ip = self.next_free_ip + 1

        while address in self.allocated_ip_addresses:
            address = self.next_free_ip
            self.next_free_ip = self.next_free_ip + 1

        network_of_address = ipaddress.ip_network(f'{address}/{self.netmask}', strict=False)
        if network_of_address.network_address != self.network.network_address:
            raise ValueError("Too many clients in that network")

        self.allocated_ip_addresses.append(address)
        return address

    def prepare(self, simulation, network_index):
        """Prepares the network.

        *Warning:* Don't call this function manually.

        Parameters
        ----------
        simulation : :class:`.Simulation`
            The simulation to prepare the network for.
        network_index : int
            The index of the network (needed for coloring).
        """
        logger.info('Preparing network (base IP: %s)', self.network)

        for channel_index, channel_prototype in enumerate(self.channels_prototypes):
            channel = channel_prototype.channel_type(self, channel_prototype.name, channel_prototype.nodes,
                                                     **channel_prototype.kwargs)
            channel_prototype.channel = channel
            self.channels.append(channel)

            if self.color is None:
                # Color is needed for a visualization.
                color = network_color_for(network_index, len(simulation.scenario.networks))
                self.color = color

        for channel in self.channels:
            logger.info('Preparing channel #%d of network %s', channel_index, self.network)
            channel.prepare(simulation)

    def set_delay(self, delay, channel_name=None):
        """Sets the delay of a specific channel (if name is present) or all channels.

        In case of WiFi-Channels, the distance between the nodes is important. The requested delay is configured at 100
        meters distance. If the distance is smaller, the delay is smaller as well (for example half of the delay at
        50 meters).

        Parameters
        ----------
        delay : str
            The new time for delay in the channel in seconds (10s) or milliseconds (10ms)
        channel_name : str
            The name of a specific channel (or all channels if value is None)
        """
        for channel in self.channels:
            if channel_name is None or channel.channel_name is channel_name:
                channel.set_delay(delay)

    def set_speed(self, speed, channel_name=None):
        """Sets the speed of a specific channel (if name is present) or all channels.

        *Warning:* So far this only has an effect before the simulation is started.

        Parameters
        ----------
        speed : str
            The new speed
        channel_name : str
            The name of a specific channel (or all channels if value is None)
        """
        for channel in self.channels:
            if channel_name is None or channel.channel_name is channel_name:
                channel.set_speed(speed)


class ChannelPrototype:
    """A channel prototype defines all parameters for the channel creation and offers a method to add nodes.

    Parameters
    ----------
    network : :class:`.Network`
        The network where the channel is located in.
    name : str
        The name of the channel.
    channel_type : class
        The channel to use.
        This can be one of :class:`.CSMAChannel` or :class:`.WiFiChannel`.
    kwargs : dict
        The parameters of the channel.
    """
    def __init__(self, network, name, channel_type, kwargs):
        self.network = network
        self.name = name
        self.channel_type = channel_type
        self.kwargs = kwargs
        self.nodes = list()
        self.channel = None  # After creation, this will be the channel object

    def connect(self, node, ip_addr=None, ifname=None):
        """Adds one node to the channel.

        Please note: Every node can only be added to one channel in the same network. Otherwise proper routing is not
        possible. Use SwitchNode to connect channels.

        Parameters
        ----------
        node : :class:`.Node`
            The node that should be connected to the network. It must be instance a subclass of :class:`.Node`.
        ip_addr : str
            The IP address of that node. If :code:`None` an random IP from the network will be assigned.
            If not :code:`None` the IP address have to be in the range of the network.
        ifname : str
            The name of the interface. If :code:`None` a random name will be assigned.
            If not :code:`None` the max. length is :code:`IFNAMSIZ` (system depended). This will not be checked.
        """
        if node in self.network.nodes and not isinstance(node, SwitchNode):
            raise ValueError("Every node can only be in one channel of a network.")

        address = None
        if ip_addr is not None:
            address = ipaddress.ip_address(ip_addr)
            self.network.allocated_ip_addresses.append(address)
        self.nodes.append(ConnectedNode(node, address, ifname=ifname))
        self.network.nodes.append(node)

    def set_delay(self, delay):
        """Sets the delay of a specific channel.

        In case of WiFi-Channels, the distance between the nodes is important. The requested delay is configured at 100
        meters distance. If the distance is smaller, the delay is smaller as well (for example half of the delay at
        50 meters).

        Parameters
        ----------
        delay : str
            The new time for delay in the channel in seconds (10s) or milliseconds (10ms)
        """
        self.channel.set_delay(delay)

    def set_speed(self, speed):
        """Sets the speed of a specific channel.

        *Warning:* So far this only has an effect before the simulation is started.

        Parameters
        ----------
        speed : str
            The new speed
        """
        self.channel.set_speed(speed)


class ConnectedNode:
    def __init__(self, node, address, ifname=None):
        self.node = node
        self.address = address
        self.ifname = ifname
