import logging
import ipaddress
import os
from ns import core, csma, internet, network as ns_net
from .interface import Interface

logger = logging.getLogger(__name__)

class Channel:

    def __init__(self, network, nodes, delay="0ms", speed="100Mbps"):
        self.network = network
        self.delay = delay
        self.speed = speed
        self.interfaces = []

        self.csma_helper = csma.CsmaHelper()

        logger.debug('Creating container with %d nodes', len(nodes))

        self.ns3_nodes_container = ns_net.NodeContainer()
        for node in nodes:
            self.ns3_nodes_container.Add(node.ns3_node)

        logger.info('Install connection between nodes')
        self.csma_helper.SetChannelAttribute("DataRate", core.StringValue(self.speed))
        self.csma_helper.SetChannelAttribute("Delay", core.StringValue(self.delay))
        self.devices_container = self.csma_helper.Install(self.ns3_nodes_container)

        logger.info('Set IP addresses on nodes')
        stack_helper = internet.InternetStackHelper()

        for i, node in enumerate(nodes):
            ns3_device = self.devices_container.Get(i)

            address = None
            if node.wants_ip_stack():
                if node.ns3_node.GetObject(internet.Ipv4.GetTypeId()) is None:
                    logger.info('Installing IP stack on %s', node.name)
                    stack_helper.Install(node.ns3_node)
                device_container = ns_net.NetDeviceContainer(ns3_device)
                ip_address = self.network.address_helper.Assign(device_container).GetAddress(0)
                netmask = network.network.prefixlen
                address = ipaddress.ip_interface(f'{ip_address}/{netmask}')

            interface = Interface(node=node, ns3_device=ns3_device, address=address)
            node.add_interface(interface)
            self.interfaces.append(interface)

    @property
    def nodes(self):
        logger.warning('Channel.nodes is deprecated')
        return list(map(lambda interface: interface.node, self.interfaces))

    def prepare(self, simulation):
        for interface in self.interfaces:
            pcap_log_path = os.path.join(simulation.log_directory, interface.pcap_file_name)
            self.csma_helper.EnablePcap(pcap_log_path, interface.ns3_device, True, True)
