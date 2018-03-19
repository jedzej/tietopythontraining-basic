import math


def distance(x1, y1, x2, y2):
    result = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))
    return result


xa = float(input('x1: '))
ya = float(input('y1: '))
xb = float(input('x2: '))
yb = float(input('y2: '))

total = distance(xa, ya, xb, yb)
print(total)
