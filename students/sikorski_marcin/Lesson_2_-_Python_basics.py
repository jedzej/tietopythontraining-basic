#-------------------
#Lesson_3
#-------------------
#Leap Year
year = int(input("Enter a year to check: "))

while year > 0:
    if (year % 400 == 0):
        print("LEAP")
        break
    else:
        if (year%4 == 0) and (year%100 != 0):
            print("LEAP")
            break
        else:
            print("COMMON")
            break

#Chocolate bar
firstValueOfPortion = int(input("Enter first value: "))
secondValueOFPortion = int(input("Enter second value: "))
numberOfSquares = int(input("Enter number of squares: "))

if (numberOfSquares%firstValueOfPortion == 0 and numberOfSquares/firstValueOfPortion < secondValueOFPortion) or (numberOfSquares%secondValueOFPortion == 0 and numberOfSquares/secondValueOFPortion < firstValueOfPortion):
    print("YES - we can divide choclate!")
else:
    print("NO - we can't divide chocolate")

#Knight move
firstColumn = int(input("Enter first column: "))
firstRow = int(input("Enter first row: "))
secondColumn = int(input("Enter second column: "))
secondRow = int(input("Enter second row: "))

row = abs(firstRow-secondRow)
column = abs(firstColumn-secondColumn)

if row == 2 and column == 1 or row == 2 and column == 1:
    print("YES - we can move there!")
else:
    print("NO - we can't move there!")

#Queen move
firstColumn = int(input("Enter first column: "))
firstRow = int(input("Enter first row: "))
secondColumn = int(input("Enter second column: "))
secondRow = int(input("Enter second row: "))

row = abs(firstRow-secondRow)
column = abs(firstColumn-secondColumn)


if row == column or firstRow == secondRow or firstColumn== secondColumn:
    print("YES - we can move the queen there!")
else:
    print("NO - we can't move queen there")

#Bishop Moves
firstColumn = int(input("Enter first column: "))
firstRow = int(input("Enter first row: "))
secondColumn = int(input("Enter second column: "))
secondRow = int(input("Enter second row: "))

row = abs(firstRow-secondRow)
column = abs(firstColumn-secondColumn)

if row == column:
    print("YES - we can move bishop there!")
else:
    print("NO - we can't move bishop there!")

#---------------------------
#Lesson 4
#---------------------------

#Lost cards
numberOfCards = int(input("Enter number of cards: "))
sumOfNumberOfCards = (((1 + numberOfCards)/2) * (numberOfCards))

sum = 0
while numberOfCards != 1:
    number = int(input("Type NOT MISSING numbers: "))
    numberOfCards -= 1
    sum += number

print("Number of lost cards: " +str(sumOfNumberOfCards-sum))

#Ladder
numberOfSteps = int(input("Enter number of steps: "))

for x in range(1, numberOfSteps + 1):
    for y in range(1, x + 1):
        print(y, sep='', end='')
    print()

#Adding factorials
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

#Tje number of zeroes
numberOfZeroes = 0

for i in range(int(input("How many numbers you want to type? "))):
    if int(input("Type the number "+ str(i+1) + "  ")) == 0:
        numberOfZeroes += 1
print("You have " + str(numberOfZeroes) + " zeroes.")

#Factorial

factorial = int(input("Type the number: "))
starter = 1

for i in range(1, factorial+1):
    starter *= i
print(starter)

#-------------------
#Lesson 6
#-------------------
# #The number of elements equal to the maximum

maximum = 0
howManyMaximumNumbers = 0
counter = 1

print("Type the numbers. Stop with 0.")

while counter != 0:
    counter = int(input())
    if counter > maximum:
        maximum, howManyMaximumNumbers = counter, 1
    elif counter == maximum:
        howManyMaximumNumbers += 1
print("Maxium number appears: " + str(howManyMaximumNumbers))