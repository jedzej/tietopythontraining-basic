#!/usr/bin/env python3

from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(distance)
