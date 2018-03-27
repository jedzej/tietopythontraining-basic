# https://snakify.org/lessons/functions/problems/length_of_segment/
# piotrsta
import math


def distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result


try:
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    print(distance(x1, y1, x2, y2))
except ValueError:
    print('Wrong value. Enter a real number.')
