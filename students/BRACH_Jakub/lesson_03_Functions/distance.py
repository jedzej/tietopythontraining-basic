from math import sqrt, pow


def distance(x1, y1, x2, y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
d = distance(x1, y1, x2, y2)
print(d)

