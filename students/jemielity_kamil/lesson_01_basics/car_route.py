import math
n = int(input("How many kilometers per day: "))
m = int(input("How many kilometres: "))

days = m / n
print(math.ceil(days))
