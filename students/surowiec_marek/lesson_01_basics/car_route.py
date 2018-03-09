import math
# Read an integers; N km/day, M km at all:
N = int(input())
M = int(input())
# Print a value How many days will it take to cover a route of length M kilometers:
print(math.ceil(M/N))
