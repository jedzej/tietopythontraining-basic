n = int(input("Adding factorials. Type n: "))
temp = 1
sumVar = 0
for i in range(1, n + 1):
    temp *= i
    sumVar += temp
print(sumVar)
