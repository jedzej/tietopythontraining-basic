#!/usr/bin/env python3

try:
    n = int(input('Please enter a number:\n'))
    if (n < 0):
        raise ValueError
except ValueError:
    print('Given number is not valid, try again')
    exit()

sum_of_factorials = 1
factorial = 1
m = n
while (m > 1):
    factorial *= n
    n -= 1
    if (n == 1):
        m -= 1
        n = m
        sum_of_factorials += factorial
        factorial = 1

print(sum_of_factorials)
