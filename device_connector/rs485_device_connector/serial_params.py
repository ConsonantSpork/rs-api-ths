from collections import Mapping

import attr
from serial import EIGHTBITS, PARITY_EVEN, STOPBITS_ONE, FIVEBITS, SIXBITS, SEVENBITS, PARITY_SPACE, PARITY_MARK, \
    PARITY_ODD, PARITY_NONE, STOPBITS_TWO, STOPBITS_ONE_POINT_FIVE


__all__ = ['SerialParams', 'SerialReceiveParams']


def port_validator(instance, attribute, value):
    if not isinstance(value, str):
        raise ValueError('Port must be a string')
    if not value.startswith('/dev/'):
        raise ValueError('Invalid port')


def baudrate_validator(instance, attribute, value):
    if int(value) <= 0:
        raise ValueError('Baud rate must be a positive integer')


def check_collection(value, collection, error_msg):
    if value not in collection:
        raise ValueError(error_msg)


def bytesize_validator(instance, attribute, value):
    check_collection(value,
                     (FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS),
                     'Invalid bytesize')


def parity_validator(instance, attribute, value):
    check_collection(value,
                     (PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE),
                     'Invalid parity')


def stopbits_validator(instance, attribute, value):
    check_collection(value,
                     (STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO),
                     'Invalid parity')


ATTRS_PARAMS = dict(repr=False, str=False, eq=False, kw_only=True, order=False, hash=False, frozen=True)


@attr.s(**ATTRS_PARAMS)
class SerialParams(Mapping):
    __unmappable__ = []

    port = attr.ib(kw_only=True, validator=port_validator)
    baudrate = attr.ib(kw_only=True, default=9600, validator=baudrate_validator)
    bytesize = attr.ib(kw_only=True, default=EIGHTBITS)
    parity = attr.ib(kw_only=True, default=PARITY_EVEN)
    stopbits = attr.ib(kw_only=True, default=STOPBITS_ONE)
    timeout = attr.ib(kw_only=True, default=2)

    def __iter__(self):
        for attrib in self.__attrs_attrs__:
            if attrib.name not in self.__unmappable__:
                yield attrib.name

    def __len__(self):
        return len(self.__attrs_attrs__)

    def __getitem__(self, attr_name):
        return self.__getattribute__(attr_name)


@attr.s(**ATTRS_PARAMS)
class SerialReceiveParams(SerialParams):
    __unmappable__ = ['to_read']

    to_read = attr.ib(kw_only=True, validator=lambda i, a, v: int(v))
