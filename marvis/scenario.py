"""The blueprint for a simulation."""

import logging

from .simulation import Simulation
from .context import Context, SimpleContext

logger = logging.getLogger(__name__)

class Scenario:
    """The scenario is kind of a blueprint for a simulation.

    A scenario can be used the following way:

    Example
    -------
    .. code-block:: python

        scenario = Scenario()
        ...
        with scenario as simulation:
            simulation.simulate(simulation_time=60)
    """

    def __init__(self):
        #: All networks belonging to the scenario.
        self.networks = set()
        #: The workflows to be executed.
        self.workflows = set()
        #: A reference to a simulation (if running).
        self.simulation = None
        #: The visualization object
        self.visualization = None

        #: The Context is e.g.\ used for teardowns.
        #:
        #: It is created on simulation start.
        self.context = None
        self.mobility_inputs = []

    def add_network(self, network):
        """Add a network to be simulated.

        Parameters
        ----------
        network : :class:`.Network`
            The Network to add.
            It will get prepared on simulation start.
        """
        self.networks.add(network)

    def add_mobility_input(self, mobility_input):
        """Add a :class:`.MobilityInput`.

        Parameters
        ----------
        mobility_input : :class:`.MobilityInput`
            The MobilityInput to add.
            It will get prepared on simulation start.
        """
        self.mobility_inputs.append(mobility_input)

    def set_visualization(self, visualization):
        """Sets the new :class:`.Visualization`.

        Parameters
        ----------
        visualization : :class:`.Visualization`
            The new visualization object.
        """
        self.visualization = visualization

    def channels(self):
        """Retrieve all channels.

        Returns
        -------
        list of :class:`.Channel`
            All channels of all networks in the current configuration.
        """
        for network in self.networks:
            for channel in network.channels:
                yield channel

    def nodes(self):
        """Retrieve all nodes

        Returns
        -------
        list of :class:`.Node`
            All nodes of all channels in the current configuration.
        """
        seen = set()
        for channel in self.channels():
            for interface in channel.interfaces:
                node = interface.node
                if node not in seen:
                    seen.add(node)
                    yield node

    def workflow(self, func):
        """Add a workflow to the scenario.

        Parameters
        ----------
        func : callable
            The callable to be executed.
        """
        self.workflows.add(func)

    def __enter__(self):
        """Prepare a new simulation and context.

        Returns
        -------
        :class:`.Simulation`
            A prepared simulation that can be started.
        """
        self.simulation = Simulation(self)
        if Context.current() is None:
            logger.warning('No context found, using SimpleContext as a fallback')
            self.context = SimpleContext()
            self.context.__enter__()
        return self.simulation

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Exit the context.

        This executes all neccessary steps in the context to clean up the simulation.
        """
        if self.context is not None:
            self.context.__exit__(exc_type, exc_value, exc_traceback)
            self.context = None
