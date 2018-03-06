#!/usr/bin/env python3

seq = ['km_per_day', 'route_km']
num = dict.fromkeys(seq)
for key in seq:
    try:
        num[key] = int(input('Please enter number of {0}:\n'.format(key)))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

if (num['route_km'] % num['km_per_day']):
    minimum_days_to_travel = num['route_km'] // num['km_per_day'] + 1
else:
    minimum_days_to_travel = num['route_km'] / num['km_per_day']

print(minimum_days_to_travel)
