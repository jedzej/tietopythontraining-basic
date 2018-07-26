# Given a non-negative integer n,//
# print the nth Fibonacci number.


def fib(n):
    if n >= 0:
        if n == 0:
            result = 0
        elif n == 1 or n == 2:
            result = 1
        else:
            result = fib(n - 1) + fib(n - 2)
        return result
    elif n < 0:
        raise ValueError
    else:
        raise TypeError

# print(fib(-6))
