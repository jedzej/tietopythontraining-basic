# Program return distance between point A and B.
import math


def distance(x1, y1, x2, y2):
    try:
        vector = math.fabs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        vector = round(vector, 5)
        print("Length of vector is:", vector)
        return vector
    except TypeError:
        print("It isn't integer!")
