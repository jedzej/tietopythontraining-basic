# The program print that Queen can change position
# from one field to second field
import math

v1 = int(input("Put vertical position for 1st field (from 1 to 8): "))
h1 = int(input("Put horizontal position for 1st field(from 1 to 8): "))
v2 = int(input("Put vertical position for 2nd field(from 1 to 8): "))
h2 = int(input("Put horizontal position for 2nd field(from 1 to 8): "))

vector_1 = int(math.fabs(v1 - v2))
vector_2 = int(math.fabs(h1 - h2))

if ((vector_1 - vector_2) == 0) & (vector_1 == 0 or vector_2 == 0):
    value = "YES"
else:
    value = "NO"

print("\nOr Queen can move from one field to second in 1 move?:", value)
