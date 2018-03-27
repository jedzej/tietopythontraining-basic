#!/usr/bin/env python3

try:
    n = int(input('Please enter a number:\n'))
    if (n < 0):
        raise ValueError
except ValueError:
    print('Given number is not valid, try again')
    exit()

factorial = 1
while (n > 1):
    factorial *= n
    n -= 1

print(factorial)
