from math import sqrt

print("The length of the segment\n")


def distance(x1, x2, y1, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = float(input("Enter the x1 coordinate of the first point: "))
y1 = float(input("Enter the y1 coordinate of the first point: "))
x2 = float(input("Enter the x2 coordinate of the second point: "))
y2 = float(input("Enter the y2 coordinate of the second point: "))

print("\nDistance between two points: {:f}".format(distance(x1, x2, y1, y2)))
