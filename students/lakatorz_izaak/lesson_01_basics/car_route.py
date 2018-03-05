import math

print("Enter car cover distance (N)")
n = int(input())

print("Enter length (M)")
m = int(input())

days = math.ceil(m / n)

print("It will take " + str(days) + " days.")
