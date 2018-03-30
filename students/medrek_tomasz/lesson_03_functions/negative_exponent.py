#!/usr/bin/env python3


def exponentiation(a, n):
    return(a ** n)


try:
    base = float(input('Please enter real number of base\n'))
    exponent = int(input('Please enter integer number of exponent\n'))
except ValueError:
    print('Not a valid number, try again')
    exit()

print(exponentiation(base, exponent))
