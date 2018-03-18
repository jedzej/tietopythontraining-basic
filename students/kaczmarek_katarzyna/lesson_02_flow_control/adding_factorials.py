n = int(input())
temp = 1
sumVar = 0
for i in range(1, n + 1):
    temp *= i
    sumVar += temp
print(sumVar)
