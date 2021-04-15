"""Ethernet LAN channel."""

import logging
import ipaddress
import os

from ns import core, csma, internet, network as ns_net

from .channel import Channel
from ..interface import Interface

logger = logging.getLogger(__name__)

class CSMAChannel(Channel):
    """The Channel resembles a physical connection of nodes.

    For CSMA this would be equivalent to one LAN cable.
    All Nodes connected to a channel will be on one collision domain.

    Parameters
    ----------
    delay : str
        A time for delay in the channel in seconds (10s) or milliseconds (10ms).
    data_rate : str
        The channel's transmission data rate.
    """

    def __init__(self, network, channel_name, nodes, delay="0ms", data_rate="100Mbps"):
        super().__init__(network, channel_name, nodes)

        #: The channel's delay.
        self.delay = delay
        #: The channel's speed for transmitting and receiving.
        #:
        #: Valid values e.g. are :code:`'100Mbps'` or :code:`'64kbps'`.
        self.data_rate = data_rate

        #: A helper for connecting nodes via CSMA.
        self.csma_helper = csma.CsmaHelper()

        #: The channel for connecting the nodes
        self.csma_channel = csma.CsmaChannel()
        self.set_delay(self.delay)
        self.set_data_rate(self.data_rate)

        #: All ns-3 devices on this channel.
        logger.info('Install connection between nodes')
        self.devices_container = self.csma_helper.Install(self.ns3_nodes_container, self.csma_channel)

        logger.info('Set IP addresses on nodes')
        stack_helper = internet.InternetStackHelper()

        for i, connected_node in enumerate(nodes):
            ns3_device = self.devices_container.Get(i)
            node = connected_node.node

            if node.wants_ip_stack():
                if node.ns3_node.GetObject(internet.Ipv4.GetTypeId()) is None:
                    logger.info('Installing IP stack on %s', node.name)
                    stack_helper.Install(node.ns3_node)
                address = connected_node.address
                if address is None:
                    address = self.network.get_free_ip_address()

                network_address = ipaddress.ip_network(f'{str(address)}/{network.netmask}', strict=False)
                ns3_network_address = ns_net.Ipv4Address(network_address.network_address)
                ns3_network_prefix = ns_net.Ipv4Mask(network_address.netmask)
                base = ipaddress.ip_address(int(address)-int(network_address.network_address))
                helper = internet.Ipv4AddressHelper(ns3_network_address, ns3_network_prefix,
                                                    base=ns_net.Ipv4Address(str(base)))
                device_container = ns_net.NetDeviceContainer(ns3_device)
                helper.Assign(device_container)
                interface = Interface(node=node, ns3_device=ns3_device,
                                      address=ipaddress.ip_interface(f'{str(address)}/{network.netmask}'))
            else:
                interface = Interface(node=node, ns3_device=ns3_device, address=connected_node.address)
            ns3_device.SetAddress(ns_net.Mac48Address(interface.mac_address))
            node.add_interface(interface, name=connected_node.ifname)
            self.interfaces.append(interface)

    def prepare(self, simulation):
        for interface in self.interfaces:
            pcap_log_path = os.path.join(simulation.log_directory, interface.pcap_file_name)
            self.csma_helper.EnablePcap(pcap_log_path, interface.ns3_device, True, True)

    def set_delay(self, delay):
        logger.info(f'Set delay of channel {self.channel_name} to {delay}')
        self.delay = delay
        if self.csma_channel is not None:
            core.Config.Set("/ChannelList/" + str(self.csma_channel.GetId()) + "/$ns3::CsmaChannel/Delay",
                            core.StringValue(str(self.delay)))

    def set_data_rate(self, data_rate):
        logger.info(f'Set speed of channel {self.channel_name} to {data_rate}')
        self.data_rate = data_rate
        if self.csma_channel is not None:
            core.Config.Set("/ChannelList/" + str(self.csma_channel.GetId()) + "/$ns3::CsmaChannel/DataRate",
                            core.StringValue(self.data_rate))
