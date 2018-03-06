#!/usr/bin/env python3

def print_help():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

def print_result(result):
    print("Result:")
    print(result)

def get_option():
    print("Enter option:")
    option = input()
    return option

def get_two_operands():
    print("Input 1st operand:")
    first_operand = float(input())
    print("Input 2nd operand:")
    second_operand = float(input())
    return first_operand, second_operand

def add():
    print("ADDING")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand + second_operand)

def subtract():
    print("SUBTRACT")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand - second_operand)

def multiply():
    print("MULTIPLY")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand * second_operand)

def divide():
    print("DIVIDE")
    first_operand, second_operand = get_two_operands()
    if second_operand == 0:
        print("Can't divide by 0!")
        return
    print_result(first_operand / second_operand)

def power():
    print("POWER")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand ** second_operand)

print("Welcome to nicely organized calculator:")
print_help()

while True:
    option = get_option()

    if option == "a":
        add()
    elif option == "s":
        subtract()
    elif option == "m":
        multiply()
    elif option == "d":
        divide()
    elif option == "p":
        power()
    elif option == "h" or option == "?":
        print_help()
    elif option == "q":
        print("GOOD BYE")
        break
    else:
        print("Invalid option!")
