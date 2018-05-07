"""
Statement
Given four real numbers representing cartesian coordinates:
(x1,y1),(x2,y2). Write a function distance(x1, y1, x2, y2) to
compute the distance between the points (x1,y1) and (x2,y2).
Read four real numbers and print the resulting distance
calculated by the function.
The formula for distance between two points can be
 found at Wolfram.
"""


import math


def distance(x1, y1, x2, y2):

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


if __name__ == "__main__":
    try:
        print("Enter four real numbers:")
        print(distance(input("Enter x1:"), input("Enter y1:"),
                       input("Enter x2:"), input("Enter y2:")))
    except ValueError:
        print("Error, invalid value")
