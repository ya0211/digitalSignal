import numpy as np
from digitalSignal.array import SignalArray, SignalElement, SignalIndex, array2t0


def _init(a: SignalArray, n=None):
    container = {"a": None, "element": None, "index": None, "n": None}
    if a.index.start() != 0:
        a = array2t0(a)
    container["a"] = a
    container["element"] = a.element
    container["index"] = a.index
    if n is not None:
        container["n"] = n
        if n > len(container["index"]):
            container["element"] += [0] * (n - len(container["index"]))
            container["index"] += [i for i in range(container["index"].stop() + 1, n)]
        else:
            container["index"] = SignalIndex([i for i in range(container["index"].start(), n)])
            container["element"] = SignalElement(a[:n])
    else:
        container["n"] = len(container["index"])

    return container


def w(container, *args, **kwargs):
    if args == tuple():
        N = container["n"]
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
    container = _init(a, n)
    if type(k) is int:
        value = sum([container["a"][index] * w(container, n=index, k=k) for index in container["index"]])
        return SignalArray([[k], [value]])
    else:
        if k is None:
            index = container["index"]
        else:
            index = k
        value = [sum([container["a"][index] * w(container, n=index, k=k)
                      for index in container["index"]]) for k in index]
        return SignalArray([index, value])
