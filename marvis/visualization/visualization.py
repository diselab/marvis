"""Visualizations to display simulation results."""

from abc import ABC, abstractmethod
from aexpr import aexpr

class Visualization(ABC):
    """The Visualization class is the abstract super class of all visualizations.

    To set a new visualization or to get the current visualization object use:

    .. code-block:: python

        from marvis.visualization import Visualization, NoVisualization
        Visualization.set_visualization(NoVisualization())
        Visualization.get_visualization().set_node_size(5.0)
    """

    __current_visualization = None

    @staticmethod
    def get_visualization():
        """Return the current visualization. Default is no visualization"""
        if Visualization.__current_visualization is None:
            Visualization.set_visualization(NoVisualization())
        return Visualization.__current_visualization

    @staticmethod
    def set_visualization(visualization):
        """Sets a new visualization.

        Parameters
        ----------
        node : :class:`.Visualization`
            The new visualization object.
        """
        Visualization.__current_visualization = visualization

    def __init__(self):
        #: The size of each node in the visualization
        self.node_size = 4
        #: The output directory
        self.output_directory = None

    def set_node_size(self, new_node_size: float):
        """Sets a new node size

        Parameters
        ----------
        new_node_size : float
            The new node size.
        """
        self.node_size = new_node_size

    def set_output_directory(self, new_output_directory: str):
        """Sets a new output directory

        Parameters
        ----------
        new_output_directory : str
            The new output directory
        """
        self.output_directory = new_output_directory

    @abstractmethod
    def prepare_node(self, node):
        """Gives the visualization the oppertunity to prepare a node

        Parameters
        ----------
        node : :class:`.Node`
            The related node.
        """
        # Every change at the position of node will be recognized
        aexpr(lambda: node.position, globals(), locals())\
        .on_change(lambda obs, oldv, newv: self.set_node_position(node, *newv))

    @abstractmethod
    def set_node_position(self, node, x, y, z=0):
        """Set the position of the node in the visualization.

        Parameters
        ----------
        node : :class:`.Node`
            The related node.
        x : float
            The x-position.
        y : float
            The y-position.
        z : float
            The z-position.
        """
        pass


class NoVisualization(Visualization):
    """The NoContext is a Null-Object and therefore **does nothing**.

    There is no visualization at all and all calls to the visualization class
    will be ignored.
    """

    def prepare_node(self, node):
        pass

    def set_node_position(self, node, x, y, z=0):
        pass
