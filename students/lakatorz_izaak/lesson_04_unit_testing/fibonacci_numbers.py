# Given a non-negative integer n, print the nth Fibonacci number. Do this by
#  writing a function fib(n) which takes the non-negative integer n and
# returns the nth Fibonacci number.


def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)