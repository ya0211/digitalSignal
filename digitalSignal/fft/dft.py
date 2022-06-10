import numpy as np
from digitalSignal.array import SignalArray, SignalElement, SignalIndex, array2t0
from .container import Container


def init(a: SignalArray, n=None) -> Container:
    self = Container(a=None, element=None, index=None, n=None)
    if a.index.start() != 0:
        a = array2t0(a)
    self.a = a
    self.element = a.element
    self.index = a.index
    if n is not None:
        self.n = n
        if n > len(self.index):
            self.element += [0] * (n - len(self.index))
            self.index += [i for i in range(self.index.stop() + 1, n)]
        else:
            self.index = SignalIndex([i for i in range(self.index.start(), n)])
            self.element = SignalElement(a[:n])
    else:
        self.n = len(self.index)

    return self.args()


def w(self, *args, **kwargs):
    if args == tuple():
        N = self.n
    else:
        N = args[0]
    if "k" not in kwargs.keys():
        k = 1
    else:
        k = kwargs["k"]
    if "n" not in kwargs.keys():
        n = 1
    else:
        n = kwargs["n"]
    return np.exp(complex(0, -2 * np.pi * n * k / N))


def dft(a: SignalArray, n=None, k=None) -> SignalArray:
    self = init(a, n)
    if type(k) is int:
        value = sum([self.a[index] * w(self, n=index, k=k) for index in self.index])
        return SignalArray([[k], [value]])
    else:
        if k is None:
            index = self.index
        else:
            index = k
        value = [sum([self.a[index] * w(self, n=index, k=k)
                      for index in self.index]) for k in index]
        return SignalArray([index, value])
