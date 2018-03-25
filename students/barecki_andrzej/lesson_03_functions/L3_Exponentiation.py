"""
Given a positive real number a and a non-negative integer n. Calculate an without using loops, ** operator
or the built in function math.pow(). Instead, use recursion and the relation an=a⋅an−1. Print the result.
"""
import os


def input_validation_positive_real():
    while True:
        print('Set a positive real number(base_value):')
        try:
            val = float(input())
            if val <= 0:
                print('Error: Value is less/equal zero.')
            else:
                break
        except ValueError:
            print('ValueError: Incorrect set of positive real number!')
    return val


def input_validation_non_negative_integer():
    while True:
        try:
            print('Set non-negative integer number(exponent_value):')
            val = int(input())
            if val < 0:
                print('Error: Value is less then zero')
            else:
                break
        except ValueError:
            print('ValueError: Incorrect set of non-negative integer number!')
    return val


def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * power(a, n - 1)


base_value = input_validation_positive_real()
exponent_value = input_validation_non_negative_integer()

res = power(base_value, exponent_value)
print("Result of expression of power is equal: {0}".format(res) + os.linesep)
