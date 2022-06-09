from .dft import _init as _init_dft
from .dft import w, dft
from digitalSignal.array import SignalArray
from scipy.fft import fft as _fft


def _init(a: SignalArray, n=None):
    _container = _init_dft(a, n)
    container = {"a": _container["a"],
                 "index": range(0, int(_container["n"] / 2)),
                 "n": _container["n"],
                 "a1": None,
                 "x1": None,
                 "a2": None,
                 "x2": None}
    container["a1"] = SignalArray(container["index"], [container["a"][i] for i in range(0, container["n"], 2)])
    container["a2"] = SignalArray(container["index"], [container["a"][i] for i in range(1, container["n"], 2)])

    if len(container["a"]) < 16:
        container["x1"] = dft(container["a1"])
        container["x2"] = dft(container["a2"])
    else:
        container["x1"] = fft1(container["a1"])
        container["x2"] = fft1(container["a2"])

    return container


def fft1(a: SignalArray, n=None, k=None):
    container = _init(a, n)
    if type(k) is int:
        if k in container["index"]:
            return container["x1"][k] + w(container, k=k) * container["x2"][k]
        else:
            return container["x1"][k] - w(container, k=k) * container["x2"][k]
    else:
        if k is None:
            element = [container["x1"][k] +
                       w(container, k=k) * container["x2"][k] for k in container["index"]] + [
                       container["x1"][k] -
                       w(container, k=k) * container["x2"][k] for k in container["index"]]
            return SignalArray(range(0, container["n"]), element)


def fft(a: SignalArray, n=None):
    container = _init_dft(a, n)
    element = _fft(container["element"])
    return SignalArray([container["index"], element])
