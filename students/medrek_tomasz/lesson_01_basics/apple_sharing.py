#!/usr/bin/env python3

seq = ['students', 'apples']
num = dict.fromkeys(seq)
for key in seq:
    try:
        num[key] = int(input('Please enter number of {0}:\n'.format(key)))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

apples_in_basket = num['apples'] % num['students']
apples_per_student = num['apples'] // num['students']

print(apples_per_student)
print(apples_in_basket)
