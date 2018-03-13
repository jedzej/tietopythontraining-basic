#1 Sum of three numbers

firstNumber = int(input())
secondNumber = int(input())
thirdNumber = int(input())
print(firstNumber+secondNumber+thirdNumber)

#2 Area of right-angled triangle
length = float(input())
height = float(input())
print(0.5*length*height)

#3 Hello, Harry!

name = input("What is your name?: ")
print("Hello, "+ name + "!")

#4 Apple sharing
numberOfStudent = int(input("How many students? "))
numberOfApples = int(input("How many apples? "))
print(numberOfApples//numberOfStudent)
print(numberOfApples%numberOfStudent)

#5 Previous and next
numberToEnter = int(input("Type some number: "))
print('The next number for the number ' + str(numberToEnter) + " is " + str(numberToEnter +1) + ".")
print('The previous number for the number ' + str(numberToEnter) + " is " + str(numberToEnter -1) + ".")

#6 School desks
numberOfStudentsInFirstClass = int(input("How many students in first class? "))
numberOfStudentsInSecondClass = int(input("How many students in second class? "))
numberOfStudentsInThirdClass = int(input("How many students in third class? "))

print("We need " + str(numberOfStudentsInFirstClass//2 + numberOfStudentsInSecondClass//2 + numberOfStudentsInThirdClass//2 + numberOfStudentsInFirstClass% 2 + numberOfStudentsInSecondClass%2 + numberOfStudentsInThirdClass%2) + " desks in total.")
#---------------------------
#PART 2
#---------------------------

#1 Last digit of integer
givenInteger = int(input())
print(givenInteger%10)

#2 Tens digit
givenIntegerNumber = int(input())
print(givenIntegerNumber//10%10)

#3 Sum of digits
threeDigetNumber = int(input("Enter a three digit number: "))
firstDigit = threeDigetNumber//100
secondDigit = threeDigetNumber//10%10
thirdDigit  = threeDigetNumber%10
print("Sum of digits equals: " + str(firstDigit+secondDigit+thirdDigit))

#4 Fractional part
import math
positiveRealNumber = float(input("Enter a positive real number to print its fractional part: "))
frac, whole = math.modf(positiveRealNumber)
print("The fractional part " + str(frac))

#5 First digit after decimal point
aPositiveRealNumber = float(input("Enter a positive real number to find the first digit after decimal point: "))
print("The first digit is " + str(int(aPositiveRealNumber*10)%10))

#6 Car route
import math
distanceCarCanTravel = int(input("Enter distance car can travel: "))
distanceToTravel = int(input("Enter distance to travel: "))
print("It will take " + str(math.ceil(distanceToTravel/distanceCarCanTravel))+ " days.")

#7 Digital clock
numberOfMinutesPassedSinceMidnight = int(input("How many minutes passed since midnight? "))
hours = numberOfMinutesPassedSinceMidnight//60
minutes = numberOfMinutesPassedSinceMidnight%60
print("On the clock there are " + str(hours) + " hours and " + str(minutes) + " minutes.")

#8 Total cost
dollars = int(input("Cupcake price in dollar is: "))
cents = int(input("Cupcake price in cents is: "))
howManyCupcakes = int(input("How many cupcakes you want to buy: "))
price = dollars + (cents/100)
howManyShouldIpay = howManyCupcakes * (100 * dollars+cents)
print("Total cost is " + str(howManyShouldIpay//100) + " dollars and " + str(howManyShouldIpay%100) + " cents.")

#9 Clock face - 1
while True:
    hours = int(input("Give me a hour between 0-12: "))
    if hours not in range(0, 13):
        print("Number must be in range 0-12!")
    else:
        break

while True:
    minutes = int(input("Give me a minutes between 0-60: "))
    if minutes not in range(0, 61):
        print("Number must be between 0-60!")
    else:
        break

while True:
    seconds = int(input("Give me a seconds between 0-60"))
    if seconds not in range(0, 61):
        print("Number must be between 0-60!")
    else:
        break

print("The angle is " + str(hours * 30 + minutes * 30 / 60 + seconds * 30 / 3600))