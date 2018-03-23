"""
Given four real numbers representing cartesian coordinates:
(x1,y1),(x2,y2). Write a function distance(x1, y1, x2, y2)
to compute the distance between the points (x1,y1) and (x2,y2).
Read four real numbers and print the resulting distance
calculated by the function.

The formula for distance between two points can be found at Wolfram.
"""

import math


def calculate_distance(x1, x2, y1, y2):
    return math.sqrt((math.pow((x2 - x1), 2)) + (math.pow((y2 - y1), 2)))


print("Calculate distance between two points:")
print("Please enter x coordinate of first point:")
x_1 = float(input())
print("Please enter y coordinate of first point:")
y_1 = float(input())
print("Please enter x coordinate of second point:")
x_2 = float(input())
print("Please enter y coordinate of second point:")
y_2 = float(input())

print("Distance between points is: " +
      str(calculate_distance(x_1, x_2, y_1, y_2)))
