#!/usr/bin/env python3

seq = ['hours', 'minutes', 'seconds']
num = dict.fromkeys(seq)
for key in seq:
    try:
        num[key] = int(input('Please enter number of {0}:\n'.format(key)))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

seconds_passed = num['seconds'] + num['minutes'] * 60 + num['hours'] * 3600
full_circle_in_seconds = 12 * 3600
angle = float(360 * seconds_passed / full_circle_in_seconds)

print(angle)
