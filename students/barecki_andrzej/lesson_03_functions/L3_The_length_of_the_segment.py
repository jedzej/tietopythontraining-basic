"""
Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2). Write a function distance(x1, y1, x2, y2)
to compute the distance between the points (x1,y1) and (x2,y2). Read four real numbers and print the resulting distance
calculated by the function.
"""
import os
import math


def input_validation():
    global value
    try:
        value = float(input())
    except ValueError:
        print('Please enter an real number!')
        input_validation()
    return value


def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


print('Set real value for points: (x1,y1) and (x2,y2)')

p1 = input_validation()
p2 = input_validation()
p3 = input_validation()
p4 = input_validation()

dist = distance(p1, p2, p3, p4)
print("Distance between (x1,y1) and (x2,y2) is equal {0:.3f}".format(dist) + os.linesep)
