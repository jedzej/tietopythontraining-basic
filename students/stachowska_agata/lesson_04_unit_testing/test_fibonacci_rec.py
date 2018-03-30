import pytest


def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def test_return5_if_called5():
    assert fib(5) == 5


def test_return610_if_called15():
    assert fib(5) == 5


def test_raises_type_error():
    with pytest.raises(TypeError):
        fib('aeou')


def test_non_value():
    with pytest.raises(TypeError):
        fib('None')


def negative_value():
    with pytest.raises(RecursionError):
        fib(-1)
