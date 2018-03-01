import math
N = int(input("How many kilometers per day: "))
M = int(input("How many kilometres: "))

days = M / N
print(math.ceil(days))