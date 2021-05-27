from enum import Enum

from device_connector.rs485_device_connector import RS485DeviceConnector


class DeviceConnector(Enum):
    RS485 = 1


def device_connector_factory(device_connector):
    if not isinstance(device_connector, DeviceConnector):
        raise ValueError(f'Device connector must be an instance of {DeviceConnector}')

    if device_connector == DeviceConnector.RS485:
        return RS485DeviceConnector()
