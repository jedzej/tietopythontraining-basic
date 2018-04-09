#!/usr/bin/env python3

seq = ['start_x', 'start_y', 'finish_x', 'finish_y']
pos = dict.fromkeys(seq)
for key in seq:
    try:
        pos[key] = int(input(
            'Please enter number of {0} position:\n'.format(key)))
        if (pos[key] < 1 or pos[key] > 8):
            raise ValueError
    except ValueError:
        print('Use single digit in range of 1 to 8, try again')
        exit()

x_diff = abs(pos['start_x'] - pos['finish_x'])
y_diff = abs(pos['start_y'] - pos['finish_y'])

if (x_diff + y_diff == 3 and x_diff < 3 and y_diff < 3):
    print('YES')
else:
    print('NO')
