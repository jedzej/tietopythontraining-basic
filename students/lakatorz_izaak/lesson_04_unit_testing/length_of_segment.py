# Write a function distance(x1, y1, x2, y2) to compute the distance between
# the points (x1,y1) and (x2,y2). Read four real numbers and print the
# resulting distance calculated by the function.

import math


def distance(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return result

