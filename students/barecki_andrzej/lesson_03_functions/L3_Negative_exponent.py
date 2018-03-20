"""
Given a positive real number a and integer n.
Write a function power(a, n) to calculate the results using the function and print the result of the expression.
Don't use the same function from the standard library.
"""
import os
import sys


def input_validation(param_type):
    global val
    if param_type == 'a':
        print('Set a positive real number:')
        try:
            val = float(input())
            if val <= 0:
                print('Error: Value is less/equal zero.')
                input_validation('a')
        except ValueError:
            print('ValueError: Incorrect set of positive real number')
            input_validation('a')
    elif param_type == 'n':
        try:
            print('Set integer number:')
            val = int(input())
        except ValueError:
            print('ValueError: Incorrect set of integer number!')
            input_validation('n')
    return val


def power(a, n):
    result = 1
    if n == 0:
        return 1
    elif n < 0:
        try:
            a = 1 / a
        except ZeroDivisionError:
            print("ZeroDivisionError")
            sys.exit()
    for _ in range(abs(n)):
        result *= a
    return result


p1 = input_validation('a')
p2 = input_validation('n')

res = power(p1, p2)
print("Result of expression power(a, n) is equal: {0}".format(res) + os.linesep)
