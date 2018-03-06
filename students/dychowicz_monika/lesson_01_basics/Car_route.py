import math

n = int(input("How many km per day?: "))
m = int(input("How many km to cover the route?: "))
print(math.ceil(m / n))
