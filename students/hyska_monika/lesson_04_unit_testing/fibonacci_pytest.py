from fibonacci import fib


def test_answer():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    assert fib(19) == 4181
    fibonacci_answer = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(2, 10):
        assert fib(i) == fibonacci_answer[i]
