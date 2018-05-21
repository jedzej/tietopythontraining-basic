#Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2). Write a function distance(x1, y1, x2, y2) to compute the distance between the points (x1,y1) and (x2,y2). Read four real numbers and print the resulting distance calculated by the function. 

import math

def distance(x1, y1, x2, y2):

    return math.sqrt( pow((x2-x1), 2) + pow((y2-y1), 2) )

print("Enter the coordinates:")
print("x1:")
x1 = float(input())
print("y1:")
y1 = float(input())
print("x2:")
x2 = float(input())
print("y2:")
y2 = float(input())

d = distance(x1, y1, x2, y2)
print(d)
