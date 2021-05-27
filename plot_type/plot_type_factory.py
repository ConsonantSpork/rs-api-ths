from enum import Enum

from plot_type.cumulative_plot_type import CumulativePlotType
from plot_type.delta_plot_type import DeltaPlotType


class PlotType(Enum):
    CUMULATIVE_PLOT = 1
    DELTA_PLOT = 2


def plot_type_factory(plot_type, plot_collection):
    if not isinstance(plot_type, PlotType):
        raise ValueError('Plot type must be an instance of PlotType')
    if plot_type == PlotType.CUMULATIVE_DATA:
        return CumulativePlotType(plot_collection)
    elif plot_type == PlotType.DELTA_DATA:
        return DeltaPlotType(plot_collection)
