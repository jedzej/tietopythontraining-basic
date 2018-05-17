# Fibonacci function.


def fib(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
        return n
    else:
        print("It isn't integer or incorrect value!")
