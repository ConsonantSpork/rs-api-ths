from abc import ABC, abstractmethod


class IDataProvider(ABC):
    """DataProvider interface.

    Represents a data source for a particular device
    """

    def __init__(self, device_id):
        self.device_id = device_id

    @abstractmethod
    def get_data(self, data_type, date_from, date_to):
        pass
