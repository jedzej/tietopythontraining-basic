#!/usr/bin/env python3
seq = ['shorter_side', 'longer_side']
length = dict.fromkeys(seq)
for key in seq:
    try:
        length[key] = int(input('Please enter length of {0}:\n'.format(key)))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

area_of_triangle = length['shorter_side'] * length['longer_side'] / 2

print(area_of_triangle)
