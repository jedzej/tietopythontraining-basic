#!/usr/bin/env python3

try:
    n = int(input('Please enter a number of numbers:\n'))
    if (n < 0):
        raise ValueError
except ValueError:
    print('Given number is not valid, try again')
    exit()

given_numbers = []
for i in range(n):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
    except ValueError:
        print('Given number is not valid, try again')
        exit()

print(given_numbers.count(0))
