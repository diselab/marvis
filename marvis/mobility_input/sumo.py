"""SUMO co-simulation."""

import logging
import os
import sys
import threading
import time

if 'SUMO_HOME' in os.environ:
    SUMO_HOME = os.environ['SUMO_HOME']
    sys.path.append(os.path.join(SUMO_HOME, 'tools'))
    os.environ['PATH'] += os.pathsep + os.path.join(SUMO_HOME, 'bin')

import traci

from .mobility_input import MobilityInput

logger = logging.getLogger(__name__)

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
    """

    def __init__(self, name="SUMO External Simulation", steps=1000,
                 sumo_host='localhost', sumo_port=8813, sumo_cmd="sumo",
                 config_path=None, step_length=1):
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

    def prepare(self, simulation):
        """Connect to SUMO server."""
        logger.info('Starting SUMO for simulation "%s".', self.name)
        if self.config_path is None:
            traci.init(host=self.sumo_host, port=self.sumo_port)
        else:
            traci.start([self.sumo_cmd, "--step-length", str(self.step_length), '-c', self.config_path])
        self.step_counter = 0

    def start(self):
        """Start a thread stepping through the sumo simulation."""
        logger.info('Starting SUMO stepping for %s.', self.name)
        def run_sumo():
            try:
                while self.step_counter < self.steps:
                    traci.simulationStep()

                    # Update positions:
                    for node in self.node_mapping:
                        x, y, z = self.__get_position_of_node(node)
                        node.set_position(x, y, z)

                    self.step_counter = self.step_counter + 1
                    time.sleep(traci.simulation.getDeltaT())
            except traci.exceptions.FatalTraCIError:
                logger.warning('Something went wrong with SUMO for %s. Maybe the connection was closed.', self.name)

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
        # Trigger abort of loop.
        self.step_counter = self.steps
        traci.close()
