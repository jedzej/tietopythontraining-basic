#!/usr/bin/env python3

import math


def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


while True:
    try:
        print("Provide coordinates")
        print("first point x: ", end='')
        x1 = float(input())
        print("first point y: ", end='')
        y1 = float(input())
        print("second point x: ", end='')
        x2 = float(input())
        print("second point y: ", end='')
        y2 = float(input())
        break
    except ValueError:
        print("It's not a valid value!")

print("Distance between (" + str(x1) + ", " + str(y1) + ") and (" + str(x2) +
      ", " + str(y2) + ") is " + str(distance(x1, y1, x2, y2)))
