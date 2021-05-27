from serial import Serial

from device_connector import IDeviceConnector
from .serial_params import SerialParams, SerialReceiveParams

from ..i_device_connector import DeviceInteractionType


__all__ = ['RS485DeviceConnector']


class RS485DeviceConnector(IDeviceConnector):
    @property
    def interaction_type(self):
        return DeviceInteractionType.SEND_RECEIVE

    def open_connection(self, connection_params):
        with Serial(**connection_params):
            return

    def send(self, data, send_params):
        with Serial(**send_params) as serial:
            serial.write(data)

    def receive(self, receive_params):
        with Serial(**receive_params) as serial:
            return serial.read(receive_params.to_read)

    @property
    def connect_params(self):
        return SerialParams

    @property
    def send_params(self):
        return SerialParams

    @property
    def receive_params(self):
        return SerialReceiveParams
