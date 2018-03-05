#!/usr/bin/env python3

print("Enter the base length")
base = input()
print("Enter the height")
height  = input()

if( height>0 and base > 0):
  area = 0.5 * base * height
  print("Area is:{0:.2f}".format(area))
else:
  print("Invalid data!")
