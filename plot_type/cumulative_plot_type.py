from plot_type.i_plot_type import IPlotType


class CumulativePlotType(IPlotType):
    def check_collection_type(self, collection):
        for prev, curr in collection:
            if prev.value > curr.value:
                return False
        return True
