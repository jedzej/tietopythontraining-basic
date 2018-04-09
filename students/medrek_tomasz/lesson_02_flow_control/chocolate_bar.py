#!/usr/bin/env python3

seq = ['squares_x', 'squares_y', 'squares_after_split']
num = dict.fromkeys(seq)
for key in seq:
    try:
        num[key] = int(input('Please enter number of {0}:\n'.format(key)))
        if (num[key] < 1):
            raise ValueError
    except ValueError:
        print('Given number is not valid, try again')
        exit()

chocolate_bar = num['squares_x'] * num['squares_y']
remaining_part = chocolate_bar - num['squares_after_split']

if (num['squares_after_split'] < chocolate_bar and
    (remaining_part % num['squares_x'] == 0 or
     remaining_part % num['squares_y'] == 0)):
    print('YES')
else:
    print('NO')
