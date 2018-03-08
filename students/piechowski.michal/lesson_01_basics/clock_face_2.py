#!/usr/bin/env python3

alpha = float(input())
time = alpha / 360 * 12
angle = (time % 1) * 360

print(angle)
