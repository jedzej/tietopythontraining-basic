# Fibonacci function.


def fib(n):
    try:
        if not(isinstance(n, int)) or n < 0:
            raise TypeError
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
        return n
    except TypeError:
        print("It isn't integer or incorrect value!")
        raise
