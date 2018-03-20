import math


def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(distance)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance(x1, y1, x2, y2)
