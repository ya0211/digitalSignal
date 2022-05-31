from ._array_utils import SignalIndex, SignalElement


class ArrayBase:
    def __init__(self, *args):
        index, element = list(), list()
        if len(args) == 1:
            if type(args[0]) is list:
                index, element = args[0]
            else:
                raise TypeError(
                    "unsupported operand type(s) :{0}".format(type(args[0])))
        elif len(args) == 2:
            index, element = args
            if len(index) != len(element):
                raise ValueError(
                    "the length index is {0}, but element's is {1}".format(len(index), len(element)))
        self.index = SignalIndex([int(i) for i in index])
        self.element = SignalElement(element)
        self._item_next = None

    def __call__(self, *args):
        self.__init__(*args)

    def __len__(self):
        return len(self.index)

    def __str__(self):
        # TODO: 更好的输出方式
        if self.index != list():
            if len(self.index) >= 2:
                return "{1}≤n≤{2}, {0}".format(self.element, self.index.start(), self.index.stop())
            else:
                return "n={1}, {0}".format(self.element[0], self.index.start())
        else:
            return "nan, {0}".format(self.element)

    def __eq__(self, other):
        # TODO: 更好的判断方式
        return other.index == self.index and other.element == self.element

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __iter__(self):
        self._item_next = self.index[0] - 1
        return self

    def __next__(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, power, modulo=None):
        pass
