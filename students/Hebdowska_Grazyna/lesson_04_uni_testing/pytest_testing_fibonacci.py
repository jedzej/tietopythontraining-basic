import pytest


def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)


def test_fibonaci_none():
    with pytest.raises(TypeError):
        fib(None)


def test_fib_aoeu():
    with pytest.raises(TypeError):
        fib('aoeu')


def test_fib_0():
    assert fib(0) == 0


def test_fib_3():
    assert fib(3) == 2


def test_fib_11():
    assert fib(11) == 89
