import math
# Read an integer:
# a = int(input())
# Print a value:
# print(a)

hour = int(input())
minute = int(input())
second = int(input())

hourAngle = float(0.5*(60*hour+minute+second/60))

print(hourAngle)
