#!/usr/bin/env python3


def exponentiation(a, n):
    if n == 0:
        return 1
    else:
        return a * exponentiation(a, n - 1)


try:
    base = float(input('Please enter real number of base\n'))
    exponent = int(input(
        'Please enter non-negative integer number of exponent\n'))
    if exponent < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, try again')
    exit()

print(exponentiation(base, exponent))
