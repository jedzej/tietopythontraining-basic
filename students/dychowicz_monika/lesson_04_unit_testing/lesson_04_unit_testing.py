import pytest


def fib(n):
    if not isinstance(n, int):
        raise TypeError("Enter the integer number")
    elif n < 0:
        raise ValueError("Enter a positive integer number")
    elif n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)

    class TestClass(object):
        def test_type(self):
            with pytest.raises(TypeError):
                fib('aoeu')

                def test_first(self):
                    assert fib(1) == 1

                    def test_zero(self):
                        assert fib(0) == 0

                        def test_negative(self):
                            with pytest.raises(ValueError):
                                fib(-2)

                                def test_float(self):
                                    with pytest.raises(TypeError):
                                        fib(0.5)


def test_standard(self):
    assert fib(6) == 8
    import unittest
    def collatz(number):
        if number % 2 == 0:
            result = number // 2
        else:
            result = 3 * number + 1
            print(result)
            return result

        class TestCollatzMethod(unittest.TestCase):
            def test_type_error(self):
                with self.assertRaises(TypeError):
                    collatz('aoeu')


def test_even(self):
    self.assertEqual(collatz(8), 4)

    def test_odd(self):
        self.assertEqual(collatz(5), 16)
        if __name__ == '__main__':
            unittest.main()


import pytest
from math import sqrt


def distance(x1, y1, x2, y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class TestClass(object):
    def test_type(self):
        with pytest.raises(TypeError):
            distance(None, None, None, None)

        def test_value(self):
            with pytest.raises(ValueError):
                distance('aoeu', 'aoeu', 'aoeu', 'aoeu')

            def test_zero_length(self):
                assert distance(0, 0, 0, 0) == 0

            def test_negative(self):
                assert distance(-1, -1, -3, -1) == 2

            def test_horizontal(self):
                assert distance(2, 0, 0, 0) == 2

                def test_vertical(self):
                    assert distance(0, 2, 0, 0) == 2

                def test_standard(self):
                    assert distance(1, 3, 2, 5) == pytest.approx(2.2, 0.1)

                    def test_order(self):
                        assert distance(1, 3, 2, 5) == distance(2, 5, 1, 3)
