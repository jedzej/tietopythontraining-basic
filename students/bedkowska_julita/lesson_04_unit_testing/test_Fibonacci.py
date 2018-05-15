import pytest


def fib(n):
    if n > 2:
        return fib(n - 1) + fib(n - 2)
    if n == 1 or n == 2:
        return 1
    if n == 0:
        return 0

# TESTS


def test_None_value():
    with pytest.raises(TypeError):
        fib(None)


def test_String_value():
    with pytest.raises(TypeError):
        fib('test')


def test_zero():
    assert fib(0) == 0


def test_one():
    assert fib(1) == 1


def test_negative_number():
    assert fib(-1) is None


def test_small_value():
    assert fib(8) == 21


def test_big_value():
    assert fib(19) == 4181
