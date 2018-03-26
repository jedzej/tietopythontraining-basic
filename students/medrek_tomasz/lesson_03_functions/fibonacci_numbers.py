#!/usr/bin/env python3


def fibonacci(n):
    if (n == 0) or (n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


try:
    number = int(input('Please enter non-negative integer number\n'))
    if number < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, try again')
    exit()

print(fibonacci(number))
