import numpy as np
from numpy import int_, float_, complex_

from ._signal_element import SignalElement
from ._signal_index import SignalIndex
from ._signal_array_str import _array_str


class SignalArray:
    def __init__(self, *args):
        index, element = list(), list()
        if len(args) == 1:
            if type(args[0]) in [list, range]:
                if len(args[0]) == 2:
                    index, element = args[0]
                else:
                    element = args[0]
                    index = range(0, len(element))
            else:
                raise TypeError(
                    "unsupported operand type(s) :{0}".format(type(args[0])))
        elif len(args) == 2:
            index, element = args
            if len(index) != len(element):
                raise ValueError(
                    "the length index is {0}, but element's is {1}".format(len(index), len(element)))
        self.index = SignalIndex(index)
        self.element = SignalElement(element)
        self._item_next = None
        self._typing = [int, float, complex, int_, float_, complex_]

    def __call__(self, *args):
        self.__init__(*args)

    def __len__(self):
        return len(self.index)

    def __str__(self):
        return _array_str(self.array())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        _self, _other = self.public(other)
        eq = list()
        for i in _self.index:
            if _self[i] == _other[i]:
                eq.append(True)
            else:
                eq.append(False)
        return "darray({0}, {1})".format(_self.index, eq)

    def _getitem_(self, start, stop):
        index_item = range(start, stop)
        element_item = list()
        for item in index_item:
            if item in self.index:
                element_item.append(self.element[self.index.index(item)])
            else:
                raise IndexError("list index out of range")
        return SignalArray([index_item, element_item])

    def public(self, other):
        public_index = list()
        for index in self.index:
            if index in other.index:
                public_index.append(index)
        self_element = self.array()[public_index[0]:public_index[-1] + 1].element
        other_element = other.array()[public_index[0]:public_index[-1] + 1].element
        return SignalArray(public_index, self_element), SignalArray(public_index, other_element)

    def __getitem__(self, item):
        if type(item) is int:
            if item in self.index:
                return self.element[self.index.index(item)]
            else:
                raise IndexError("list index out of range")
        elif type(item) is slice:
            if item.start is not None:
                if item.stop is not None:
                    return self._getitem_(item.start, item.stop)
                else:
                    return self._getitem_(item.start, self.index[-1] + 1)
            else:
                if item.stop is not None:
                    return self._getitem_(self.index[0], item.stop)
                else:
                    return self.array()

    def __setitem__(self, key, value):
        if type(key) is slice:
            if key.start is None:
                start = self.index.start()
            else:
                start = key.start
            if key.stop is None:
                stop = self.index.stop()
            else:
                stop = key.stop
            if type(value) is list:
                value = [i for i in value]
                if len(self.array()[key]) == len(value):
                    stop = self.index.index(stop)
                    if key.stop is None:
                        stop += 1
                    self.element[self.index.index(start):stop] = value
                else:
                    raise IndexError("list index out of range")
            else:
                raise TypeError("unsupported operand type(s): {0}".format(type(value)))
        elif type(key) is int:
            self.element[self.index.index(key)] = value

    def __next__(self):
        self._item_next += 1
        if self._item_next == self.index[-1] + 1:
            raise StopIteration
        else:
            return [self._item_next, self.array()[self._item_next]]

    def __add__(self, other):
        if type(other) is SignalArray:
            _self, _other = self.public(other)
            element = [_self[i] + _other[i] for i in _self.index]
            return SignalArray([_self.index, element])
        elif type(other) in self._typing:
            return SignalArray([self.index,
                                [self.array()[i] + other for i in self.index]])
        else:
            raise TypeError("supported operand type(s) for +: 'int', 'float', 'complex' and 'SignalArray'")

    def __sub__(self, other):
        if type(other) is SignalArray:
            _self, _other = self.public(other)
            element = [_self[i] - _other[i] for i in _self.index]
            return SignalArray([_self.index, element])
        elif type(other) in self._typing:
            return SignalArray([self.index,
                                [self.array()[i] - other for i in self.index]])
        else:
            raise TypeError("supported operand type(s) for -: 'int', 'float', 'complex' and 'SignalArray'")

    def __mul__(self, other):
        if type(other) is SignalArray:
            _self, _other = self.public(other)
            element = [_self[i] * _other[i] for i in _self.index]
            return SignalArray([_self.index, element])
        elif type(other) in self._typing:
            return SignalArray([self.index,
                                [self.array()[i] * other for i in self.index]])
        else:
            raise TypeError("supported operand type(s) for *: 'int', 'float', 'complex' and 'SignalArray'")

    def __pow__(self, power, modulo=None):
        if type(power) is SignalArray:
            _self, _other = self.public(power)
            element = [_self[i] ** _other[i] for i in _self.index]
            return SignalArray([_self.index, element])
        elif type(power) in self._typing:
            return SignalArray([self.index,
                                [self.array()[i] ** power for i in self.index]])
        else:
            raise TypeError("supported operand type(s) for **: 'int', 'float', 'complex' and 'SignalArray'")

    def __abs__(self):
        if type(self.element[0]) in [complex, complex_]:
            return SignalArray([self.index,
                                [np.sqrt(self.element[i].real ** 2 + self.element[i].imag ** 2) for i in self.index]])
        else:
            return self.array()

    def reverse(self):
        index = range(-self.index[-1], -self.index[0] + 1)
        element = [self.element[i] for i in range(-1, -len(self.element) - 1, -1)]
        return SignalArray(index, element)

    def shift(self, n: int):
        index = range(self.index[0] - n, self.index[-1] + 1 - n)
        element = self.element
        return SignalArray(index, element)

    def array(self):
        return SignalArray(self.index, self.element)

    def phase(self):
        element = list()
        for i in self.index:
            if self.element[i].real != 0:
                element.append(np.arctan(self.element[i].imag / self.element[i].real))
            else:
                element.append(0)
        return SignalArray([self.index, element])

    def round(self, decimals):
        for i in self.index:
            if type(self.element[i]) in [float, np.float64]:
                self.element[i] = np.round(self.element[i], decimals)
            else:
                real = np.round(self.element[i].real, decimals)
                imag = np.round(self.element[i].imag, decimals)
                if real == 0:
                    real = 0
                if imag == 0:
                    imag = 0
                self.element[i] = complex(real, imag)

        return self.array()
