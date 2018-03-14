# Read an integer:
import math

n = int(input("How many kilometers per day?"))
m = int(input("How many kilometers to cover?"))

print(math.ceil(m / n))
