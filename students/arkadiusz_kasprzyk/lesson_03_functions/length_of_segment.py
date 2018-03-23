import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


x1 = float(input("Give x1: "))
y1 = float(input("Give y1: "))
x2 = float(input("Give x2: "))
y2 = float(input("Give y2: "))

print("Distance between points is {}.".format(distance(x1, y1, x2, y2)))
