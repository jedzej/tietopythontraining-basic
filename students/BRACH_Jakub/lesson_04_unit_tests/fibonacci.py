import pytest


def test_CornerCase_TyperError_for_no_parameter():
    with pytest.raises(TypeError):
        fib(None)


def test_CornerCase_TypeError_for_string():
    with pytest.raises(TypeError):
        fib("aoeu")


def test_CornerCase_for_negative_input():
    assert fib(-1) == "error"


def test_normal_for_0():
    assert fib(0) == 0


def test_normal_for_1():
    assert fib(1) == 1


def test_normal_for_10():
    assert fib(10) == 55


def test_normal_for_10():
    assert fib(20) == 6765


def fib(n):
    if n < 0:
        return "error"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

