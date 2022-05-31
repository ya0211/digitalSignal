from .array_base import ArrayBase


class SignalArray(ArrayBase):
    def __init__(self, *args):
        super().__init__(*args)

    def _getitem(self, start, stop):
        _element_item = list()
        for item in range(start, stop):
            if item in self.index:
                _element_item.append(self.element[self.index.index(item)])
            else:
                raise IndexError("list index out of range")
        return _element_item

    def _public(self, other):
        public_index = list()
        for index in self.index:
            if index in other.index:
                public_index.append(index)
        self_element = self.array()[public_index[0]:public_index[-1]+1]
        other_element = other.array()[public_index[0]:public_index[-1]+1]
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
                    return self._getitem(item.start, item.stop)
                else:
                    return self._getitem(item.start, self.index[-1]+1)
            else:
                if item.stop is not None:
                    return self._getitem(self.index[0], item.stop)
                else:
                    return self.element

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
                value = [float(i) for i in value]
                if len(self.array()[key]) == len(value):
                    stop = self.index.index(stop)
                    if key.stop is None:
                        stop += 1
                    self.element[self.index.index(start):stop] = value
                else:
                    raise IndexError("list index out of range")
            else:
                raise IndexError("list index out of range")
        elif type(key) is int:
            if type(value) is int:
                value = float(value)
            self.element[self.index.index(key)] = value

    def __next__(self):
        self._item_next += 1
        if self._item_next == self.index[-1] + 1:
            raise StopIteration
        else:
            return [self._item_next, self.array()[self._item_next]]

    def __add__(self, other):
        if type(other) is SignalArray:
            _self, _other = self._public(other)
            element = [_self[i] + _other[i] for i in _self.index]
            return SignalArray([_self.index, element])
        elif type(other) is int or type(other) is float or type(other) is complex:
            return SignalArray([self.index,
                                [self.array()[i] + other for i in self.index]])
        else:
            raise TypeError("supported operand type(s) for +: 'int', 'float', 'complex' and 'SignalArray'")

    def __mul__(self, other):
        if type(other) is SignalArray:
            _self, _other = self._public(other)
            element = [_self[i] * _other[i] for i in _self.index]
            return SignalArray([_self.index, element])
        elif type(other) is int or type(other) is float:
            return SignalArray([self.index,
                                [self.array()[i] * other for i in self.index]])
        else:
            raise TypeError("supported operand type(s) for *: 'int', 'float', and 'SignalArray'")

    def __pow__(self, power, modulo=None):
        if type(power) is SignalArray:
            _self, _other = self._public(power)
            element = [_self[i] ** _other[i] for i in _self.index]
            return SignalArray([_self.index, element])
        elif type(power) is int or type(power) is float:
            return SignalArray([self.index,
                                [self.array()[i] ** power for i in self.index]])
        else:
            raise TypeError("supported operand type(s) for **: 'int', 'float', and 'SignalArray'")

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
