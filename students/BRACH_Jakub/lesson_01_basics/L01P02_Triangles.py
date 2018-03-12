#!/usr/bin/env python3

#print("Enter the base length")
base = float(input())
#print("Enter the height")
height  = float(input())

if height > 0 and base > 0:
  area = 0.5 * base * height
  print("{0:.2f}".format(area))
else:
  print("Invalid data!")

