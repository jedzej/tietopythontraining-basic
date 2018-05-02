import pytest


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def test_for_5():
    assert fib(5) == 5


def test_for_15():
    assert fib(15) == 610


def test_raises_type_error():
    with pytest.raises(TypeError):
        fib('aeou')


def test_non_value():
    with pytest.raises(TypeError):
        fib('None')
