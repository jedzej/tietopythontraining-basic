from fib_num import fib


def test_fib_1():
    assert fib(1) == 1


def test_fib_2():
    assert fib(8) == 21


def test_fib_3():
    assert fib(10) == 55


def test_fib_4():
    assert fib(20) == 6765
