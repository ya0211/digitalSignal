from digitalSignal.array import SignalArray, SignalElement, SignalIndex, array2t0
import numpy as np


class DFT:
    def __init__(self, a=None, n=None):
        self.dfs_array = None
        if a is not None:
            if a.index.start() != 0:
                a = array2t0(a)
            self.a = a
            self.element = a.element
            self.index = a.index
            if n is None:
                self.n = len(self.index)
            else:
                self.n = n
                if n > len(self.index):
                    self.element += [0] * (n - len(self.index))
                    self.index += [i for i in range(self.index.stop()+1, n)]
                else:
                    self.index = SignalIndex([i for i in range(self.index.start(), n)])
                    self.element = SignalElement(a[:n])

    def __call__(self, a=None, n=None):
        self.__init__(a, n)

    def _dft_k(self, k, index):
        real = self.a[index] * np.cos(2 * np.pi * index * k / self.n)
        imag = - self.a[index] * np.sin(2 * np.pi * index * k / self.n)
        return complex(real, imag)

    def dft(self, a=None, n=None, k=None) -> SignalArray:
        if a is not None:
            self.__init__(a, n)
        if type(k) is int:
            value = sum([self._dft_k(k, index) for index in self.index])
            self.dfs_array = SignalArray([[k], [value]])
        else:
            if k is None:
                index = self.index
            else:
                index = k
            k_element = list()
            for i in index:
                value = sum([self._dft_k(i, index) for index in self.index])
                k_element.append(value)
            self.dfs_array = SignalArray([index, k_element])
        return self.dfs_array

    def abs(self, a=None, n=None, k=None) -> SignalArray:
        if a is not None:
            self.__init__(a, n)
        if k is not None:
            self.dft(k=k)
        else:
            if self.dfs_array is None:
                self.dft()
        dfs = self.dfs_array
        k_index, k_element = dfs.index, dfs.element
        k_element = [np.sqrt(e.real ** 2 + e.imag ** 2) for e in k_element]
        return SignalArray(k_index, k_element)

