import math
number = int(input())

a = number - number // 10 * 10
b = math.floor(number / 10) - math.floor(number / 10) // 10 * 10
c = math.floor(number / 100)
print(a + b + c)
