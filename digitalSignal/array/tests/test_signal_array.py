import unittest
from digitalSignal.array.signal_array import SignalArray

a = SignalArray(range(-1, 4), [10, 2, 4, 5, 8])


class TestSignalArray(unittest.TestCase):

    def test_init(self):
        global a
        b = SignalArray([range(-1, 4), [10, 2, 4, 5, 8]])
        self.assertTrue(a == b)

    def test_call(self):
        global a
        darray = SignalArray
        b = darray(range(-1, 4), [10, 2, 4, 5, 8])
        self.assertTrue(a == b)

    def test_len(self):
        global a
        self.assertEqual(len(a), 5)

    def tear_str(self):
        pass

    def test_eq(self):
        pass

    def test_getitem(self):
        global a
        self.assertListEqual(a[0:2], [2.0, 4.0])
        self.assertListEqual(a[1:], [4.0, 5.0, 8.0])
        self.assertListEqual(a[:2], [10.0, 2.0, 4.0])
        self.assertListEqual(a[:], [10.0, 2.0, 4.0, 5.0, 8.0])

    def test_setitem(self):
        b = a.array()
        b[1] = 12
        self.assertListEqual(b.element, [10.0, 2.0, 12.0, 5.0, 8.0])
        b[1:] = [4, 5, 8]
        self.assertListEqual(b.element, [10.0, 2.0, 4.0, 5.0, 8.0])
        b[:1] = [2, 10]
        self.assertListEqual(b.element, [2.0, 10.0, 4.0, 5.0, 8.0])
        b[:] = [11, 2, 4, 5, 8]
        self.assertListEqual(b.element, [11.0, 2.0, 4.0, 5.0, 8.0])

    def test_add(self):
        global a
        b = SignalArray([range(0, 4), [2, 4, 5, 8]])
        self.assertTrue(a + b == b + a and a + b == SignalArray([range(0, 4), [4, 8, 10, 16]]))
        self.assertTrue(a + 1 == 1 + a and a + 1 == SignalArray([range(-1, 4), [11, 3, 5, 6, 9]]))

    def test_mul(self):
        global a
        b = SignalArray([range(0, 4), [2, 4, 5, 8]])
        self.assertTrue(a * b == b * a and a * b == SignalArray([range(0, 4), [4, 16, 25, 64]]))
        self.assertTrue(a * 2 == 2 * a and a * 2 == SignalArray([range(-1, 4), [20, 4, 8, 10, 16]]))

    def test_pow(self):
        global a
        self.assertTrue(a ** 3 == SignalArray([range(-1, 4), [1000, 8, 64, 125, 512]]))
