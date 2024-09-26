numberToCheck = int(input("Give me a number to do facorial" ))

whichFactorial = 1
sum=0

if numberToCheck != 0:
    for i in range (1, numberToCheck+1):
        whichFactorial *= i
        sum += whichFactorial
    print(sum)
else:
    print(1)