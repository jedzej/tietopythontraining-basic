"""
Given a positive real number a and a non-negative integer n. Calculate an without using loops, ** operator
or the built in function math.pow(). Instead, use recursion and the relation an=a⋅an−1. Print the result.
"""
import os


def input_validation(param_type):
    global val
    if param_type == 'a':
        print('Set a positive real number(a):')
        try:
            val = float(input())
            if val <= 0:
                print('Error: Value is less/equal zero.')
                input_validation('a')
        except ValueError:
            print('ValueError: Incorrect set of positive real number!')
            input_validation('a')
    elif param_type == 'n':
        try:
            print('Set non-negative integer number(n):')
            val = int(input())
            if val < 0:
                print('Error: Value is less then zero')
                input_validation('n')
        except ValueError:
            print('ValueError: Incorrect set of non-negative integer number!')
            input_validation('n')
    return val


def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * power(a, n - 1)


p1 = input_validation('a')
p2 = input_validation('n')

res = power(p1, p2)
print("Result of expression power(a, n) is equal: {0}".format(res) + os.linesep)
