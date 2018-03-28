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
