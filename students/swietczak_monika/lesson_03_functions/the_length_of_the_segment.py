from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


a = float(input("Enter x1: "))
b = float(input("Enter y1: "))
c = float(input("Enter x2: "))
d = float(input("Enter y2: "))
print(distance(a, b, c, d))
