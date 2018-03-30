lastNo = int(input())
sumFactorial = 1
for i in range(lastNo):
    sumFactorial += i * sumFactorial
print(sumFactorial)
