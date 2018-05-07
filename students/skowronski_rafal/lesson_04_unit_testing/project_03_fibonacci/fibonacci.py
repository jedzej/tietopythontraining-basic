'''Provides access to Fibonacci function'''


def fibonacci(n):
    '''Returns value of the n-th of the Fibonacci sequence'''

    if not isinstance(n, int):
        raise TypeError

    if n <= 0:
        raise ValueError

    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
