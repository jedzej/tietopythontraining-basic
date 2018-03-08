from math import floor

print("Enter minutes passed:")
n = int(input())

hours = floor(n/60)
mins = n % 60

print(str(hours) + " " + str(mins))
