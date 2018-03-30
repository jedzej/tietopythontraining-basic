"""
Given a non-negative integer n, print the nth Fibonacci number. Do this by writing a function fib(n) which takes
the non-negative integer n and returns the nth Fibonacci number.
Don't use loops, use the flair of recursion instead. However, you should think about why the recursive method is much
slower than using loops.
"""
import os


def input_validation():
    while True:
        try:
            print('Set non-negative integer number(n):')
            val = int(input())
            if val < 0:
                print('Error: Value is less then zero')
            else:
                break
        except ValueError:
                print('ValueError: Incorrect set of integer number!')
    return val


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


param = input_validation()
res = fib(param)
print("Fibonacci number is equal: {0}".format(res) + os.linesep)
