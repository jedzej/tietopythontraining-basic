#!/usr/bin/env python3

H = int(input())
M = int(input())
S = int(input())

angle = (H + M / 60 + S / 3600) / 12 * 360
print(angle)
