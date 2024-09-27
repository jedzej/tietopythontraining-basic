#The length of segment

import math

def distance(x1,y1,x2,y2):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    print(distance)

first_x = float(input("Type first X: "))
first_y = float(input("Type first Y: "))
second_x = float(input("Type second X: "))
second_y = float(input("Type second Y: "))

print(distance(first_x,first_y,second_x,second_y))

#Negative exponent
def power(a,n):
    if n == 0:
        print(1)
    else:
        print(a**n)

while True:
    real_number = int(input("Type real, positive number"))
    if realNumber <= 0:
        print("I said POSITIVE")
        continue
    else:
        real_power = int(input("Now type power: "))
        print(power(real_number, real_power))
        break

#Exponentiation
def exponentiation(value, to_the_power):
    if to_the_power == 0:
        return 1
    else:
        return value * exponentiation(value, to_the_power-1)

print(exponentiation(float(input("Type number: ")), int(input("To the power of: "))))

#Fibonacci numbers
def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1)+ fib(x-2)

which_number_user_wants_to_calculate = float(input("Which Fibonnaci number you want to see? "))

print(fib(which_number_user_wants_to_calculate))

#The Collatz Sequence
def collatz(number):
        if number % 2 == 0:
            return number//2
        elif number % 2 ==1:
            return 3 * number + 1
        else:
            print("What sort of input is this???")

number_to_check = float(input("Enter a number for a collatz sequence: "))
is_this_number_one = collatz(number_to_check)

print(number_to_check)
print(is_this_number_one)
while is_this_number_one != 1:
    print(collatz(is_this_number_one))
    is_this_number_one = collatz(is_this_number_one)

#Input Validation
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
    else:
        print("What sort of input is this???")

while True:
    try:
        number_to_check = float(input("Enter a number for a collatz sequence: "))
        break
    except ValueError:
        print("This is not a number")

isThisNumberOne = collatz(number_to_check)

print(number_to_check)
print(is_this_number_one)
while is_this_number_one != 1:
    print(collatz(is_this_number_one))
    is_this_number_one = collatz(is_this_number_one)

#Calculator
print(input("Welcome to badly organized calculator: "
            "\na - add"
            "\ns - subtract"
            "\nm - multiply"
            "\nd - divide"
            "\np - power"
            "\nh,? - help"
            "\nq - QUIT"))

def adding(addX, addY):
    print("ADDING\nResult: " + str(addX + addY))

def subtract(subX, subY):
    print("SUBTRACT\nResult: " + str(subX - subY))

def multiply(mulX, mulY):
    print("MULTIPLY\nResult: " + str(mulX * mulY))

def divide(divX, divY):
    print("DIVIDE\nResult: " + str(divX / diivY))

def power(powX, powY):
    print("POWER\nResult: " + str(powX ** powY))

def help():
    input("HELP "
          "\na - add"
          "\ns - subtract"
          "\nm - multiply"
          "\nd - divide"
          "\np - power"
          "\nh,? - help"
          "\nq - QUIT")

def bye():
    print("GOOD BYE")

while True:
    option = str(input("Enter option:"))
    firstValue = int(input("Input 1st operand:"))
    secondValue = int(input("Input 2st operand:"))

    if option == "a":
        adding(firstValue, secondValue)
    elif option == "s":
        subtract(firstValue, secondValue)
    elif option == "m":
        multiply(firstValue, secondValue)
    elif option == "d":
        divide(firstValue, secondValue)
    elif option == "p":
        power(firstValue, secondValue)
    elif option == "h":
        help()
    elif option == "?":
        help()
    elif option == "q":
        bye()
        break
    else:
        break