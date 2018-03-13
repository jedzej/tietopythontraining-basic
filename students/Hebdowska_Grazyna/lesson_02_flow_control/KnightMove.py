import math
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

if (abs(x2 - x1) == 2) and (abs(y2 - y1) == 1):
    print('yes')
elif (abs(x2 - x1) == 1) and (abs(y2 - y1) == 2):
    print('yes')
else:
    print('no')
