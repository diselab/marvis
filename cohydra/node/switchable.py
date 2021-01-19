import logging
import requests

logger = logging.getLogger(__name__)

class SwitchableWrapper:

    def __init__(self, wrapped_node, channel, bridge_address):
        self.wrapped_node = wrapped_node
        self.bridge_address = bridge_address
        self.channel = channel

    def switch_on(self):
        try:
            response = requests.put(self.bridge_address + '/socket/' + str(self.channel) + '/on')
            logger.info('Calling PUT on %s/socket/%s/on', str(self.bridge_address), str(self.channel))
        except requests.ConnectionError:
            logger.warning('Could not connect to bridge at %s', str(self.bridge_address))
            return
        if response.status_code is not 200:
            logger.warning('Could not switch on switchable node %s on channel %s', str(self.wrapped_node), str(self.channel))
        else:
            logger.info('Physically switched on node %s', self.wrapped_node)
        return

    def switch_off(self):
        try:
            response = requests.put(self.bridge_address + '/socket/' + str(self.channel) + '/off')
            logger.info('Calling PUT on %s/socket/%s/off', str(self.bridge_address), str(self.channel))
        except requests.ConnectionError:
            logger.warning('Could not connect to bridge at %s', str(self.bridge_address))
            return
        if response.status_code is not 200:
            logger.warning('Could not switch off switchable node %s on channel %s', str(self.wrapped_node), str(self.channel))
        else:
            logger.info('Physically switched off node %s', self.wrapped_node)
        return
