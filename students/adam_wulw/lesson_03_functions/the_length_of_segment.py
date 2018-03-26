import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


x1 = float(input('x1\n'))
y1 = float(input('y1\n'))
x2 = float(input('x2\n'))
y2 = float(input('y2\n'))
print(distance(x1, y1, x2, y2))
