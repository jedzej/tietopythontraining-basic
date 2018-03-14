# https://snakify.org/lessons/functions/problems/length_of_segment/
# piotrsta
import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result

print(distance(x1, y1, x2, y2))
