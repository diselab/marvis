"""Physical hosts to connect to via SSH."""

import logging
import ipaddress
import paramiko

from pyroute2 import IPRoute

from ..command_executor import SSHCommandExecutor
from .external import ExternalNode

logger = logging.getLogger(__name__)

def default_ip(ifname):
    """Calculates the default IP address.

    This takes the subnet and adds 1.

    Parameters
    ----------
    ifname : str
        The name of the interface.
    """
    ipr = IPRoute()
    index = ipr.link_lookup(ifname=ifname)[0]
    addr = ipr.get_addr(index=index)[0]
    interface = ipaddress.ip_interface('{}/{}'.format(addr.get_attr('IFA_ADDRESS'), addr['prefixlen']))
    addr = interface.ip + 1
    if addr in interface.network:
        return str(addr)
    raise TypeError(f'Unable to calculate default node ip in {ifname} ({interface})')

class SSHNode(ExternalNode):
    """An SSH node represents an external device reachable via SSH.

    Parameters
    ----------
    username : str
        The username used to login onto the device.
    password : str
        The password for the given user.
    """

    def __init__(self, name, ip=None, bridge=None, ifname='eth0', username='pi', password='raspberry'):
        super().__init__(name, bridge=bridge, ifname=ifname)

        if ip is None:
            ip = default_ip(bridge)

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(ip, username=username, password=password)
        self.command_executor = SSHCommandExecutor(name, client, sudo=True)
