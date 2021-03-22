"""NetAnim Visualization using the NetAnim format."""

import os
from ns import netanim

from .visualization import Visualization

class NetAnimVisualization(Visualization):
    """The NetAnimVisualization class produces a netanim.xml file which
    contains visualization details in the NetAnim format.

    To create a NetAnim visualization, use the following code and hand the
    object to the scenario.

    .. code-block:: python

        from marvis.visualization.netanimvisualization import NetAnimVisualization
        visualization = NetAnimVisualization()
        visualization.set_node_size(5.0)
        scenario.set_visualization(visualization)
    """

    def __init__(self):
        super().__init__()

        #: The netanim animation interface
        self.animation_interface = None

    def prepare_node(self, node):
        super().prepare_node(node)
        self._prepare()
        self.animation_interface.UpdateNodeDescription(node.ns3_node, node.name)
        if node.color:
            self.animation_interface.UpdateNodeColor(node.ns3_node, *node.color)
        self.animation_interface.UpdateNodeSize(
            node.ns3_node.GetId(),
            self.node_size,
            self.node_size
        )

    def set_node_position(self, node, x, y, z=0):
        netanim.AnimationInterface.SetConstantPosition(node.ns3_node, x, y, z)

    def _prepare(self):
        if self.animation_interface is None:
            self.animation_interface = netanim.AnimationInterface(os.path.join(self.output_directory, "netanim.xml"))
            self.animation_interface.EnablePacketMetadata(True)
