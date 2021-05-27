from abc import abstractmethod, ABCMeta
from enum import Enum
from functools import wraps


def validate_params(operation_type):
    """Decorator to validate operation parameters against schema."""

    def outer(func):
        @wraps(func)
        def inner(*args):
            self = args[0]
            params = args[-1]
            validation_class = getattr(self, f'{operation_type}_params')
            try:
                return func(*args[:-1], validation_class(**params))
            except TypeError as e:
                raise TypeError(f'Invalid {operation_type} parameters') from e

        return inner

    return outer


class DeviceConnectorMcs(ABCMeta):
    def __new__(cls, name, bases, attr):
        # Decorate methods of subclasses with validate_params
        attr['open_connection'] = validate_params('connect')(
            attr['open_connection']
        )
        attr['send'] = validate_params('send')(
            attr['send']
        )
        attr['receive'] = validate_params('receive')(
            attr['receive']
        )


class DeviceInteractionType(Enum):
    SEND_RECEIVE = 1
    RECEIVE_ONLY = 2


# class IDeviceConnector(metaclass=DeviceConnectorMcs):
class IDeviceConnector:
    """Device locator interface.

    Represents an abstract device address
    """

    @property
    @abstractmethod
    def interaction_type(self):
        pass

    @abstractmethod
    def open_connection(self, connection_params):
        """Establish connection to device.

        Check device availability and prepare to communicate with it.
        Raises RuntimeException if device is unavailable.
        """

        pass

    @abstractmethod
    def send(self, data, send_params):
        """Send data to device."""

        pass

    @abstractmethod
    def receive(self, receive_params):
        """Receive data from device."""

        pass

    @property
    def connect_params(self):  # Name of this property is used in validate_params decorator
        return DefaultConnectParams

    @property
    def send_params(self):  # Name of this property is used in validate_params decorator
        return DefaultConnectParams

    @property
    def receive_params(self):  # Name of this property is used in validate_params decorator
        return DefaultConnectParams


class DefaultConnectParams:
    """Default connection parameters."""

    pass


class DefaultSendParams:
    """Default send parameters."""

    pass


class DefaultReceiveParams:
    """Default receive parameters."""

    pass
