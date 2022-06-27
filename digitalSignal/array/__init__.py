from ._signal_element import SignalElement
from ._signal_index import SignalIndex
from ._signal_array import SignalArray as _SignalArray
from ._periodic_extend import expand, getT

__all__ = ["SignalArray", "SignalElement", "SignalIndex"]
__all__ += ["expand", "getT"]


class SignalArray(_SignalArray):
    def getT(self):
        return getT(self.array())

    def expand(self, n, t=1):
        return expand(self.array(), n, t)
