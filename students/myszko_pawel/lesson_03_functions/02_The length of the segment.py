# Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2).
# Write a function distance(x1, y1, x2, y2) to compute the distance between the
# points (x1,y1) and (x2,y2). Read four real numbers and print the resulting
# distance calculated by the function. The formula for distance between two
# points can be found at Wolfram.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def distance(a, b, c, d):
    distance = ((c - a) ** 2 + (d - b) ** 2) ** (.5)
    print(distance)


distance(x1, y1, x2, y2)
