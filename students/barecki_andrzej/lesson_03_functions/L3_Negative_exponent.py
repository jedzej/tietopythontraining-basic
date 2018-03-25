"""
Given a positive real number a and integer n.
Write a function power(a, n) to calculate the results using the function and print the result of the expression.
Don't use the same function from the standard library.
"""
import os
import sys


def input_validation_positive_real():
    while True:
        print('Set a positive real number:')
        try:
            val = float(input())
            if val <= 0:
                print('Error: Value is less/equal zero.')
            else:
                break
        except ValueError:
            print('ValueError: Incorrect set of positive real number')
    return val


def input_validation_integer():
    while True:
        try:
            print('Set integer number:')
            val = int(input())
            break
        except ValueError:
            print('ValueError: Incorrect set of integer number!')
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


base_value = input_validation_positive_real()
exponent_value = input_validation_integer()

res = power(base_value, exponent_value)
print("Result of expression power(a, n) is equal: {0}".format(res) + os.linesep)
