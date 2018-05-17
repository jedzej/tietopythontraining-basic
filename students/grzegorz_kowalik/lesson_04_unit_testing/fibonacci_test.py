import pytest
from students.grzegorz_kowalik.lesson_03_functions import fibonacci


def test_type_error():
    with pytest.raises(TypeError):
        fibonacci.fib('aoeu')


def test_zero():
    assert 0 == fibonacci.fib(0)


def test_one():
    assert 1 == fibonacci.fib(1)


def test_five():
    assert 5 == fibonacci.fib(5)


def test_ten():
    assert 55 == fibonacci.fib(10)
