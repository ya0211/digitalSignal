from typing import Any, Union, Optional

from numpy import int_, float_, complex_

from ._signal_element import SignalElement
from ._signal_index import SignalIndex


class SignalArray:
    def __init__(self, *args: Union[range, list]) -> None:
        self.index = SignalIndex
        self.element = SignalElement
        self._item_next = Union[int]
        self._typing = Union[list]

    def __call__(self, *args: Union[range, list]) -> None:...

    def __len__(self) -> int:...

    def __str__(self) -> str:...

    def __repr__(self) -> str:...

    def __eq__(self, other: SignalArray) -> str:...

    def _getitem_(self, start: int, stop: int) -> SignalArray:...

    def public(self, other: SignalArray) -> tuple[SignalArray, SignalArray]:...

    def __getitem__(self, item: Union[int, slice]) -> SignalArray:...

    def __setitem__(self, key: Union[int, slice], value: Any) -> None:...

    def __next__(self) -> list[int, Any]:...

    def __add__(self, other: Union[int, float, complex, int_, float_, complex_, SignalArray]) -> SignalArray:...

    def __sub__(self, other: Union[int, float, complex, int_, float_, complex_, SignalArray]) -> SignalArray:...

    def __mul__(self, other: Union[int, float, complex, int_, float_, complex_, SignalArray]) -> SignalArray:...

    def __pow__(self, power: Union[int, float, complex, int_, float_, complex_, SignalArray], modulo=None) -> SignalArray:...

    def __abs__(self) -> SignalArray:...

    def reverse(self) -> SignalArray:...

    def shift(self, n: int) -> SignalArray:...

    def array(self) -> SignalArray:...

    def phase(self) -> SignalArray:...

    def round(self, decimals: int) -> SignalArray:...

    def expand(self, n: int, t: Optional[int] = 1) -> SignalArray:...

    def getT(self) -> SignalArray:...