
def fib(n):

    if isinstance(n, str):
        raise ValueError

    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
