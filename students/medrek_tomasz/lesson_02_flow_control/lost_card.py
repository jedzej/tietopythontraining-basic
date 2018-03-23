#!/usr/bin/env python3

try:
    n = int(input('Please enter a number of cards:\n'))
    if (n < 1):
        raise ValueError
except ValueError:
    print('Given number is not valid, try again')
    exit()

given_numbers = []
for i in range(n - 1):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
        if (given_numbers[i] < 1 or given_numbers[i] > n):
            raise ValueError
    except ValueError:
        print('Given number is not valid, try again')
        exit()

for i in range(1, n + 1):
    if i not in given_numbers:
        print(i)
