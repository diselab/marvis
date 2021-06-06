"""SUMO co-simulation."""

import logging
import os
import sys
import threading
import time

from .mobility_input import MobilityInput
from .mobility_provider import MobilityProvider
from .mobility_provider_server import RPCMobilityProviderServer

from .null_lock import NullLock

# Include SUMO tools to path to access TraCI or Libsumo
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")


# =================================================================================
# The SUMO mobility input can be controlled by two ways:
# * TraCI
# * Libsumo
#
# TraCI allows to start or connect to SUMO and communicate via sockets. Even though multiple TraCI clients can connect to the same SUMO server, this method is not suitable for mobility providers running in a separate thread. Simulation will only proceed if all clients called `simulationStep()`, which is a blocking function.
# Connection objects can be shared, but the methods are not thread safe. Access to TraCI therefore needs to be managed via synchronization objects. It is not yet analyzed, how large numbers of request for `SumoMobilityProvider` influence the simulation execution, as they might block the simulation due to the shared connection. In this case, using Libsumo and `NullLock`s can prevent this problem.
# 
# Libsumo allows to use SUMO as a library without the overhead of sockets and similar techniques. However, this method is limited, e.g. no support for SUMO-GUI. Because of its library-style, functions can be called in different threads. Therefore, synchronization is not necessary and a `NullLock` can be used to avoid changing the source code to remove synchronization calls.
#
# Find more information here:
# TraCI: https://sumo.dlr.de/docs/TraCI.html
# Libsumo: https://sumo.dlr.de/docs/Libsumo.html
# =================================================================================


USE_LIBSUMO = False

if USE_LIBSUMO:
    import libsumo as traci
else:
    import traci

logger = logging.getLogger(__name__)

class SumoMobilityProvider(MobilityProvider):
    """
    SumoMobilityProvider is an interface for applications to get traffic simulation data or influence the simulation.

    The SumoMobilityProvider will be wrapped by a server to serve traffic requests.
    """

    def __init__(self, lock):
        # A lock object to access a shared connection
        # This might be necessary when using TraCI
        self.lock = lock
        self.logger = logging.getLogger(__name__ + ".mobility_provider")

    def getVehicleDetails(self, vehId):
        self.lock.acquire()

        try:
            vehicleIsActive = vehId in traci.vehicle.getIDList()
            vehicle_details = {
                "isVehicleActive": 0 if not vehicleIsActive else 1,
                "position3d": (0.0, 0.0, 0.0) if not vehicleIsActive else traci.vehicle.getPosition3D(vehId),
                "speed": 0.0 if not vehicleIsActive else traci.vehicle.getSpeed(vehId),
                # From ETSI TS 102 894-2:
                # The value shall be set to 1022 if the vehicle length is equal to or greater than 102,2 metres.
                "lengthInCentimeter": 0 if not vehicleIsActive else min(1022, int(traci.vehicle.getLength(vehId) * 10))
            }
        except traci.exceptions.TraCIException as e:
            self.logger.error(f"Caught TraCI exception. {e.getType()}: {e} Command: {e.getCommand()}")
        except traci.exceptions.FatalTraCIError as e:
            self.logger.error(f"Fatal TraCI error caught for {self.name}. Reason: {e}.")
        except Exception:
            pass
        self.lock.release()

        return vehicle_details

    def stopAtEndOfCurrentSegment(self, vehId, duration=0):
        self.lock.acquire()
        try:
            end_of_road_segment = traci.lane.getLength(traci.vehicle.getLaneID(vehId))
            traci.vehicle.setStop(
                vehId,
                traci.vehicle.getRoadID(vehId),
                pos=end_of_road_segment,
                laneIndex=traci.vehicle.getLaneIndex(vehId),
                duration=1.0*duration
            )
        except traci.exceptions.TraCIException as e:
            self.logger.error(f"Caught TraCI exception. {e.getType()}: {e} Command: {e.getCommand()}")
        except traci.exceptions.FatalTraCIError as e:
            self.logger.error(f"Fatal TraCI error caught for {self.name}. Reason: {e}.")
        except Exception:
            pass
        self.lock.release()

    def resumeOrCancelStop(self, vehId):
        self.lock.acquire()
        try:
            if traci.vehicle.isStopped(vehId):
                traci.vehicle.resume(vehId)
            else:
                end_of_road_segment = traci.lane.getLength(traci.vehicle.getLaneID(vehId))
                traci.vehicle.setStop(
                    vehId,
                    traci.vehicle.getRoadID(vehId),
                    pos=end_of_road_segment,
                    laneIndex=traci.vehicle.getLaneIndex(vehId),
                    duration=0.0
                )
        except traci.exceptions.TraCIException as e:
            self.logger.error(f"Caught TraCI exception. {e.getType()}: {e} Command: {e.getCommand()}")
        except traci.exceptions.FatalTraCIError as e:
            self.logger.error(f"Fatal TraCI error caught for {self.name}. Reason: {e}.")
        except Exception:
            pass
        self.lock.release()

class SUMOMobilityInput(MobilityInput):
    """SUMOMobilityInput is an interface to the SUMO simulation environment.

    This mobility input supports two modes:

    * | **Remote Mode**: In this mode the testbed connects to an external already running SUMO instance.
      | You configure the host and port where the SUMO server is running via the ``sumo_host`` and ``sumo_port``
        argument.
    * | **Local Mode**: In this mode the testbed starts a locally installed version of SUMO.
      | You configure the simulation via the ``sumo_cmd`` and ``config_path`` argument.
        If SUMO is not installed globally you need to set the ``SUMO_HOME`` environment variable.
      | **Warning: This does not work when using marvis in the prebuilt docker containers.**
        For instructions on how to use marvis without Docker,
        please refer to :ref:`Local Installation Without Docker` and :ref:`Install SUMO On Simulation Host`.

    Parameters
    ----------
    name : str
        The name of the MobilityInput.
    steps : int
        The number of steps to run the SUMO simulation.
    sumo_host : str
        The host on which the SUMO simulation is running.
    sumo_port : int
        The TraCI port.
    sumo_cmd : str
        The command to start sumo when using the local mode (default: ``sumo``).
    config_path : str
        The path to the simulation configuration (.cfg).
    steplength : float
        The length of each simulation step in seconds (default: 1).
        It only has effect in the local mode.
    rpc_server_config : tuple
        Starts a rpc server if value is not None.
        The tuple needs three elements: (ip, port, log_requests).
    """

    def __init__(self, name="SUMO External Simulation", steps=1000,
                 sumo_host='localhost', sumo_port=8813, sumo_cmd="sumo",
                 config_path=None, step_length=1, rpc_server_config=None):
        super().__init__(name)
        #: The host on which the SUMO simulation is running.
        #:
        #: When running on a devcontainer, this is probably ``localhost``.
        self.sumo_host = sumo_host
        #: The TraCI port.
        #:
        #: Can be specified on the server with the ``--remote-port`` option.
        self.sumo_port = sumo_port
        #: The command to start sumo locally
        self.sumo_cmd = sumo_cmd
        #: The path to the simulation scenario configuration.
        self.config_path = config_path
        #: The number of steps to simulate.
        self.steps = steps
        #: The length of every simulation step
        self.step_length = step_length
        #: The number of steps to simulate in SUMO.
        self.step_counter = 0
        #: The RPC server if rpc_server_config is not None
        self.rpc_server = None
        #: The connection details of the RPC server
        self.rpc_server_config = rpc_server_config
        #: The lock to acquire traci connection
        self.lock = NullLock() if USE_LIBSUMO else threading.Lock()

    def prepare(self, simulation):
        """Connect to SUMO server."""
        logger.info('Starting SUMO for simulation "%s".', self.name)
        if self.config_path is None:
            traci.init(host=self.sumo_host, port=self.sumo_port)
        else:
            traci.start([self.sumo_cmd, "--step-length", str(self.step_length), '-c', self.config_path])
        self.step_counter = 0

        if self.rpc_server_config is not None:
            logger.info(f"Starting RPC server on {self.rpc_server_config[0]}:{self.rpc_server_config[1]}. Logs requests: {self.rpc_server_config[2]}")
            self.rpc_server = RPCMobilityProviderServer(self.rpc_server_config, SumoMobilityProvider, (self.lock))

    def start(self):
        """Start a thread stepping through the sumo simulation."""
        logger.info('Starting SUMO stepping for %s.', self.name)
        def run_sumo():
            try:
                while self.step_counter < self.steps:
                    self.lock.acquire()
                    traci.simulationStep()
                    step_start_time = time.time()

                    # Update positions:
                    ids = list()
                    ids.extend(traci.vehicle.getIDList())
                    ids.extend(traci.person.getIDList())
                    ids.extend(traci.junction.getIDList())

                    for node in self.node_mapping:
                        if self.node_mapping[node][0] not in ids:
                            continue
                        
                        x, y, z = self.__get_position_of_node(node)
                        node.set_position(x, y, z)

                    self.step_counter = self.step_counter + 1
                    delta_t = traci.simulation.getDeltaT()
                    time_this_step = time.time() - step_start_time
                    self.lock.release()
                    time.sleep(max(0, delta_t - time_this_step))
            except traci.exceptions.TraCIException as e:
                logger.error(f"Caught TraCI exception. {e.getType()}: {e} Command: {e.getCommand()}")
            except traci.exceptions.FatalTraCIError as e:
                logger.error(f"Fatal TraCI error caught for {self.name}. Reason: {e}.")
                sys.exit(1)

        thread = threading.Thread(target=run_sumo)
        thread.start()

    def add_node_to_mapping(self, node, sumo_vehicle_id, obj_type="vehicle"):
        self.node_mapping[node] = (sumo_vehicle_id, obj_type)

    def __get_position_of_node(self, node):
        if node not in self.node_mapping:
            raise "Unknown node "+str(node.name)
        if self.node_mapping[node][1] == "person":
            return traci.person.getPosition3D(self.node_mapping[node][0])
        if self.node_mapping[node][1] == "vehicle":
            return traci.vehicle.getPosition3D(self.node_mapping[node][0])
        if self.node_mapping[node][1] == "junction":
            # Junction has no support for 3D positions
            x, y = traci.junction.getPosition(self.node_mapping[node][0])
            return x, y, 0.0
        raise "Unknown type " + str(self.node_mapping[node][1])

    def destroy(self):
        """Stop SUMO."""
        logger.info('Trying to close SUMO for %s.', self.name)
        # Abort SUMO simulation loop
        self.step_counter = self.steps
        # Stop RPC mobility provider server
        self.rpc_server.stop()
        if self.lock.locked():
            self.lock.release()
        # Stop SUMO and TraCI
        traci.close()
