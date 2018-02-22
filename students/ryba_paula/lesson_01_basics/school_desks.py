import math

a = int(input())
b = int(input())
c = int(input())

#print((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))
print(math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2))