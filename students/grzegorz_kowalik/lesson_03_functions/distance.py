from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


x1 = float(input("x1 "))
x2 = float(input("x2 "))
y1 = float(input("y1 "))
y2 = float(input("y2 "))

print(distance(x1, x2, y1, y2))
