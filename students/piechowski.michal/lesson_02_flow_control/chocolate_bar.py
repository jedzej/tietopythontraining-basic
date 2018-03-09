#!/usr/bin/env python3

width = int(input())
height = int(input())
number_of_squares = int(input())

if ((number_of_squares % width == 0 or number_of_squares % height == 0)
        and width * height >= number_of_squares):
    print('YES')
else:
    print('NO')

