from typing import TypeVar

import numpy as np
from numpy import int_, float_, complex_

SignalArray = TypeVar("SignalArray")


def _array_str(a: SignalArray) -> str:
    _len_a = len(a)
    _str_index = "darray {0}".format(a.index.range())
    _str_array = _str_index
    _str_element = ""
    for item in a.element:
        if len(_str_element) >= 60:
            _str_array += '\n'
            _str_array += _str_element
            _str_element = ""
        if type(item) in [complex, complex_]:
            _real = np.round(item.real, 8)
            _str_element += "{:08f}".format(_real).rjust(15, " ")
            _imag = np.round(item.imag, 8)
            if _imag == 0:
                _imag = 0
            if _imag >= 0:
                _imag = "+{:08f}".format(_imag)
            else:
                _imag = "{:08f}".format(_imag)
            _str_element += "{0}j".format(_imag).ljust(15, " ")
        elif type(item) in [float, float_]:
            _item = np.round(item.real, 8)
            _str_element += "{:08f}".format(_item).rjust(15, " ")
        elif type(item) in [int, int_]:
            _str_element += " {}".format(item).rjust(len(str(a.element.max()))+1, " ")
    if _str_array == _str_index:
        _str_array += " [{}]".format(_str_element)
    return _str_array

