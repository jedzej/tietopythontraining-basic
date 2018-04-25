import math


def distance(a, b, c, d):
    w = math.sqrt((a - c) ** 2 + (b - d) ** 2)
    return w


x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print("%.5f" % distance(x1, y1, x2, y2))
