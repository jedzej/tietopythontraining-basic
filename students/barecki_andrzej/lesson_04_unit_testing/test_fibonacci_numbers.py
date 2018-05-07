import pytest


"""Unit Under Test"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def test_typeerror_when_called_none_on_function_fib():
    """Test that it crashes with TypeError when called on None"""
    with pytest.raises(TypeError):
        fib(None)


def test_typeerror_when_called_aoue_on_function_fib():
    """Test that it crashes with ValueError when called on 'aoeu'"""
    with pytest.raises(TypeError):
        fib('aoeu')


def test_fib_0():
    assert fib(0) == 0


def test_fib_1():
    assert fib(1) == 1


def test_fib_2():
    assert fib(2) == 1


def test_fib_3():
    assert fib(3) == 2


def test_fib_4():
    assert fib(4) == 3


def test_fib_5():
    assert fib(5) == 5


def test_recursion_error_for_fib():
    try:
        fib(-100)
    except RuntimeError as exception:
        assert str(exception) == 'maximum recursion depth exceeded' \
                                 ' in comparison'
