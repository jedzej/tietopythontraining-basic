lastNo = int(input())
sumOfAllFactorials = 0
for number in range(lastNo):
    singuleFactorial = 1
    for factorial in range(number):
        singuleFactorial += (factorial + 1) * singuleFactorial
    sumOfAllFactorials += singuleFactorial
print(sumOfAllFactorials)