"""Visualization offers multiple visualizations and
has an interface for user defined visualizations.
"""
from .visualization import Visualization, NoVisualization
# Do not import NetAnimVisualization here, since otherwise it would load the dependencies
