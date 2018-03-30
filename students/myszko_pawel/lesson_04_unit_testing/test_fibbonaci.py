import pytest
from fibbonaci import fib


def test_none():
    with pytest.raises(TypeError):
        fib(None)

def test_string():
    with pytest.raises(TypeError):
        fib('aeou')
        
def test_1():
    assert fib(1) == 1

def test_2():
    assert fib(2) == 1

def test_3():
        assert fib(3) == 2

def test_4():
    assert fib(4) == 3

def test_5():
    assert fib(5) == 5

def test_6():
    assert fib(6) == 8


if __name__ == '__main__':
    unittest.main()
