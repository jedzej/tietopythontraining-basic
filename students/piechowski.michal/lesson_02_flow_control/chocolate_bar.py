#!/usr/bin/env python3

width = int(input())
height = int(input())
number_of_squares = int(input())

if width * height < number_of_squares:
    print('NO')
elif number_of_squares % width == 0 or number_of_squares % height == 0:
    print('YES')
else:
    print('NO')

