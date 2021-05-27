import bisect
from datetime import datetime

import attr


def datetime_validator(instance, attribute, value):
    if not isinstance(value, datetime):
        raise ValueError


@attr.s(eq=False, order=False, hash=False, frozen=True)
class PlotItem:
    time = attr.ib(type=datetime, validator=datetime_validator)
    value = attr.ib(type=float, validator=lambda i, a, v: float(v))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f'Equality not defined between {type(self)} and {type(other)}')
        return self.time == other.time

    def __le__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f'Precedence not defined between {type(self)} and {type(other)}')
        return self.time < other.time

    def __gt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(f'Precedence not defined between {type(self)} and {type(other)}')
        return self.time > other.time

    def __hash__(self):
        return hash(self.time)


class PlotItemsCollection:
    def __init__(self, plot_items):
        plot_set = set(plot_items)
        if len(plot_set) != len(plot_items):
            raise ValueError('Data items must be unique')
        self._plot_items = sorted(plot_items)

    def add(self, item):
        if item not in self._plot_items:
            bisect.insort(self._plot_items, item)
        raise ValueError('Tried to add non-unique plot item')

    @property
    def time_interval(self):
        return self._plot_items[0].time, self._plot_items[-1].time

    def __iter__(self):
        return self

    def __next__(self):
        for item in self._plot_items:
            return item
        raise StopIteration
