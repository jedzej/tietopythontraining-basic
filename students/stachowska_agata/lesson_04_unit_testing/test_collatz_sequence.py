import pytest


def collatz(x):
    if x % 2 == 0:
        res = x // 2
    else:
        res = 3 * x + 1
    return res


def test_return4_if_called8():
    assert collatz(8) == 4


def test_return16_if_called5():
    assert collatz(5) == 16


def test_raises_type_error():
    s = 'aeou'
    with pytest.raises(TypeError):
        collatz(s)
