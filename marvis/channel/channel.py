"""Abstract Channel class."""
import logging

from ns import network as ns_net

logger = logging.getLogger(__name__)

class Channel:
    """The Channel resembles a physical connection of nodes.

    For CSMA this would be equivalent to one LAN cable.
    All Nodes connected to a channel will be on one collision domain.

    *Warning:* Do not instantiate a channel yourself.
        Use the network's capabilities to link nodes.

    Parameters
    ----------
    network : :class:`.Network`
        The network this channel belongs to.
    channel_name : str
        The name of the channel
    nodes : list of :class:`.Node`
        The nodes to connect on a physical channel.
    """

    def __init__(self, network, channel_name, nodes):
        if len(nodes) < 2:
            raise ValueError(f"The channel {channel_name} has less than 2 nodes. Abort.")

        #: The network the channel belongs to.
        self.network = network

        #: The name of the channel
        self.channel_name = channel_name

        #: All Interfaces (~network cards) on this channel.
        self.interfaces = []

        logger.debug('Creating container with %d nodes', len(nodes))
        #: A container with all ns-3 internal nodes.
        self.ns3_nodes_container = ns_net.NodeContainer()
        for connected_node in nodes:
            self.ns3_nodes_container.Add(connected_node.node.ns3_node)

    @property
    def nodes(self):
        """Return all nodes of this channel.

        Returns
        -------
        list of :class:`.Node`
            The list of nodes in this channel.
        """
        logger.warning('Channel.nodes is deprecated. Use ??? instead.')
        return list(map(lambda interface: interface.node, self.interfaces))

    def prepare(self, simulation):
        """Prepare the channel (for logging).

        Parameters
        ----------
        simulation : :class:`.Simulation`
            The simulation to prepare the channel for.
        """
        raise NotImplementedError
