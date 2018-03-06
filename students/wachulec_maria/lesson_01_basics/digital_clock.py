from math import floor

N = int(input("N: "))

hours = floor(N/60)
minutes = N - (hours * 60)
print(hours, minutes)
