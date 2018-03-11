import math
a = int(input())
temp = math.floor(a / 10)
print(temp - (temp // 10) * 10)
