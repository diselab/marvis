"""Base abstract class for co-simulation positional input."""

class MobilityInput:
    """A MobilityInput can be used to control multiple node's positions via an external positional simulation.

    Parameters
    ----------
    name : str
        The name of the MobilityInput.
        This does not have to be unique. It is used for logging debugging purposes.
    """

    def __init__(self, name):
        #: The name of the input.
        self.name = name

        #: The mapping of simulation nodes to IDs identifying the nodes in the external simulation interface
        self.node_mapping = {}

    def prepare(self, simulation):
        """Prepare the external simulation if neccessary.

        Parameters
        ----------
        simulation : :class:`.Simulation`
            The simulation that is going to run.
        """
        raise NotImplementedError

    def start(self):
        """This function gets called on simulation start."""
        raise NotImplementedError

    def destroy(self):
        """Stop external simulations or any other teardowns."""
        raise NotImplementedError
