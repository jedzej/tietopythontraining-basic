import math

n = int(input())
m = int(input())

w1 = m // n
w2 = (m - n * w1) / m

print(w1 + math.ceil(w2))
