#!/usr/bin/env python3

try:
    n = int(input('Please enter a number:\n'))
    if (n < 1):
        raise ValueError
except ValueError:
    print('Given number is not valid, try again')
    exit()

message = ""

for i in range(1, n + 1):
    message += str(i)
    print(message)
