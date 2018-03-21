#!/usr/bin/env python3

try:
    year = int(input('Please enter number of year:\n'))
    if (year < 0):
        raise ValueError
except ValueError:
    print('Given number is not valid, try again')
    exit()

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print('LEAP')
else:
    print('COMMON')
