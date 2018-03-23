import math

x1 = float(input('Give x1: '))
y1 = float(input('Give y1: '))
x2 = float(input('Give x2: '))
y2 = float(input('Give y2: '))


def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


print('{} {}'.format('Distance:', distance(x1, y1, x2, y2)))
