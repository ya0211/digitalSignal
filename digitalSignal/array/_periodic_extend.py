from typing import Optional

import numpy as np

from ._signal_array import SignalArray


def expand(a: SignalArray, n: int, t: Optional[int] = 1) -> SignalArray:
    if a.index.start != 0:
        a = getT(a)
    if n < np.ceil(len(a) / 2):
        raise ValueError(
            "the n={0} is too small, n≥{1}".format(n, int(np.ceil(len(a) / 2))))
    index = a.index
    index = range(index.start(), n * t)
    if len(a) <= n:
        element = a.element + [0] * (n - len(a))
        element = element * t
        return SignalArray(index, element)
    else:
        element_1 = a.element[:n]
        element_2 = a.element[n:]
        element = [element_1[i] + element_2[i] for i in range(0, len(a) - n)] + element_1[len(a) - n:]
        element = element * t
        return SignalArray(index, element)


def getT(a: SignalArray) -> SignalArray:
    index = a.index
    element = a.element
    t = len(a)
    n = 1
    if index.start() < 0:
        index_t0 = range(index.start(), index.stop() + t * n + 1)
        while t not in index_t0:
            n += 1
            index_t0 = range(index.start(), index.stop() + t * n + 1)
        element_t0 = element + element * n
        element_t0 = SignalArray(index_t0, element_t0)[0:t].element
        return SignalArray(range(0, t), element_t0)
    else:
        index_t0 = range(index.start() - t * n, index.stop() + 1)
        while 0 not in index_t0:
            n += 1
            index_t0 = range(index.start() - t * n, index.stop() + 1)
        element_t0 = element + element * n
        element_t0 = SignalArray(index_t0, element_t0)[0:t].element
        return SignalArray(range(0, t), element_t0)
