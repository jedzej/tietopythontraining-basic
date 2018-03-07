import math

#Problem1: Sum of numbers
print("We will count the Sum of three numbers")
print("Please write first number")
firstNumber = int(input())
print("Your choice is: " + str(firstNumber))
print("Please write second number")
secondNumber = int(input())
print("Your choice is: " + str(secondNumber))
print("Please write third number")
thirdNumber = int(input())
print("Your choice is: " + str(thirdNumber))
print("Your choose numbers: " + str(firstNumber) + ", " + str(secondNumber) + ", " + str(thirdNumber))
sum = firstNumber + secondNumber + thirdNumber
print("The sum of yours numbers is: " + str(int(sum)))
print("THE END of Sum numbers problem")
print("")

#Problem2: Area of right-angled triangle
print("We will count the area of right-angled triangle")
print("Please write length of the base:")
base = int(input())
print("Please write the high of right-angle triangle:")
high = int(input())
area = (base * high)//2
print("The area of right-angle triangle is: " + str(area))
print("THE END of Area of right-angled triangle problem")
print("")

#Problem3: Hello, Harry!
print("We will print Hello, Harry greetings")
print("Hello stranger. Could you please write your name:")
strangerName = str(input())
print("Hello, "+strangerName+"!")
print("THE END of Hello, Harry! problem")
print("")

#Problem4: Apple sharing
print("We will share the apples")
print("Please provide quantity of students:")
N = int(input())
print("Please provide quantity of apples")
K = int(input())
studentApples = K // N
basketApples = K % N
print("Each student will get: " + str(studentApples) + " apples.")
print("There will be " + str(basketApples) + " apples left in the basket")
print("THE END of Apple sharing problem")
print("")

#Problem5: Previous and next
print("We will print previous and next number")
print("Please provide the number:")
number = int(input())
previous = number - 1
next = number + 1
print("The previous number is: " + str(previous))
print("The next number is: " + str(next))
print("THE END of Previous and next problem")
print("")

#Problem6: School desks
print("We will count quantity of needed desks")
print("Please provide the quantity of students in first class:")
studentsFirstClass = int(input())
print("Please provide the quantity of students in second class:")
studentsSecondClass = int(input())
print("Please provide the quantity of students in third class:")
studentsThirdClass = int(input())
deskFirstClass = math.ceil(studentsFirstClass/2)
deskSecondClass = math.ceil(studentsSecondClass/2)
deskThirdClass = math.ceil(studentsThirdClass/2)
print("For first class we would need: " + str(deskFirstClass) + " desk")
print("For second class we would need: " + str(deskSecondClass) + " desk")
print("For third class we would need: " + str(deskThirdClass) + " desk")
print("THE END of School desks problem")
print("")
