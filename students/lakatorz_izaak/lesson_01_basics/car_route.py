from math import ceil

print("Enter car cover distance (N)")
n = int(input())

print("Enter length (M)")
m = int(input())

days = ceil(m / n)

print("It will take " + str(days) + " days.")