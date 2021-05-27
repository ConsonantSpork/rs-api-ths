from abc import ABC, abstractmethod


class IPlotType(ABC):
    def __init__(self, plot_items_collection):
        if not self.check_collection_type(plot_items_collection):
            raise ValueError(f'Invalid plot collection for {type(self)}')
        self._collection = plot_items_collection

    @abstractmethod
    def check_collection_type(self, collection):
        """Check that collection satisfies collection type requirements.

        E.g. for cumulative plot check that every plot item's value is greater
        or equal to the previous.

        :param collection plot_type.plot_items.DataItemsCollection collection to check

        :return bool indicating check success
        """

        pass

    @property
    def collection(self):
        return self._collection
