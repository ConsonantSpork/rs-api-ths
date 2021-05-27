from plot_type.i_plot_type import IPlotType


class DeltaPlotType(IPlotType):
    def check_collection_type(self, collection):
        return all(item.value > 0 for item in collection)
