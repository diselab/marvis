import logging
import threading

from xmlrpc.server import SimpleXMLRPCServer

logger = logging.getLogger(__name__)

class RPCMobilityProviderServer:
    """
    RPCMobilityProviderServer is a RPC server which wraps an `MobilityProvider` to serve traffic requests.
    The RPC server will be started in a separate thread.

    Parameters
    ----------
    connection_details : tuple
        A tuple containing connection information: (ip, port, log_requests)
    mobility_provider_cl : class
        The class of the MobilityProvider to be wrapped.
    mobility_provider_args : tuple
        Arguments that will be passed to the mobility_provider on instantiation
    """
    def __init__(self, connection_details, mobility_provider_cl, mobility_provider_args=()):

        self.server = SimpleXMLRPCServer(connection_details[:2], logRequests=connection_details[2], allow_none=True)
        
        self.mobility_handler = threading.Thread(target=self.run, args=[mobility_provider_cl, self.server, mobility_provider_args])
        self.mobility_handler.setDaemon(True)  # Daemonize thread
        self.mobility_handler.start()  # Start the execution

    def run(self, mobility_provider_cl, server, mobility_provider_args):
        """Creates a `MobilityProvider` instance and registers it to serve requests."""
        mobility_provider_inst = mobility_provider_cl(mobility_provider_args)
        server.register_instance(mobility_provider_inst, allow_dotted_names=True)
        server.serve_forever()

    def stop(self):
        """Stops the RPC server and waits for the containing thread to join."""
        logger.info("Shutting down server")
        self.server.shutdown()
        self.mobility_handler.join()

