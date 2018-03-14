from math import ceil
# Read number of kilometers a car can cover per day (N)
# and the length of kilometers (M)
N = int(input())
M = int(input())
# Print the number of days needed by the car to cover the route
print(ceil(M/N))
