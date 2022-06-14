from typing import Optional

from scipy.fft import fft as _fft

from digitalSignal.array import SignalArray
from ._container import Container
from ._dft import init as _init
from ._dft import w, dft


def init(a: SignalArray, n: Optional[int] = None) -> Container:
    _self = _init(a, n)
    self = Container(a=_self.a,
                     n=_self.n,
                     index=range(0, int(_self.n / 2)),
                     a1=None,
                     x1=None,
                     a2=None,
                     x2=None)

    self.a1 = SignalArray(self.index, [self.a[i] for i in range(0, self.n, 2)])
    self.a2 = SignalArray(self.index, [self.a[i] for i in range(1, self.n, 2)])

    if len(self.a) < 4:
        self.x1 = dft(self.a1)
        self.x2 = dft(self.a2)
    else:
        self.x1 = fft1(self.a1)
        self.x2 = fft1(self.a2)

    return self.args()


def fft1(a: SignalArray, n: Optional[int] = None) -> SignalArray:
    self = init(a, n)
    element = [self.x1[k] + w(self, k=k) * self.x2[k] for k in self.index] + [
                  self.x1[k] - w(self, k=k) * self.x2[k] for k in self.index]
    return SignalArray(range(0, self.n), element)


def fft(a: SignalArray, n: Optional[int] = None) -> SignalArray:
    self = _init(a, n)
    element = _fft(self.element)
    return SignalArray([self.index, element])
