#!/usr/bin/env python3

seq = ['dollars', 'cents', 'cupcakes']
num = dict.fromkeys(seq)
for key in seq:
    try:
        num[key] = int(input('Please enter number of {0}:\n'.format(key)))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

cost = dict.fromkeys(['dollars', 'cents'])
cost['cents'] = num['cupcakes'] * num['cents'] % 100
cost['dollars'] = num['cupcakes'] * num['cents'] // 100 \
                + num['cupcakes'] * num['dollars']

print('{dollars} {cents}'.format(**cost)) #format_map doesnt work in snakify
