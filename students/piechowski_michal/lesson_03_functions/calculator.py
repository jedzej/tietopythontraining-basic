#!/usr/bin/env python3

""" Simple python calculator. """


def print_help():
    """ Explains options used in the script. """
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def print_result(result):
    """ Prints given result. """
    print("Result:")
    print(result)


def get_option():
    """ Returns option choosen by the user. """
    option = input("Enter option: ")
    return option


def get_two_operands():
    """ Returns two operands used later for calculations. """
    first_operand = float(input("Input 1st operand: "))
    second_operand = float(input("Input 2nd operand: "))
    return first_operand, second_operand


def add():
    """ Adds two numbers. """
    print("ADDING")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand + second_operand)


def subtract():
    """ Subtracts two numbers. """
    print("SUBTRACT")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand - second_operand)


def multiply():
    """ Multiplies two numbers. """
    print("MULTIPLY")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand * second_operand)


def divide():
    """ Divides two numbers. """
    print("DIVIDE")
    first_operand, second_operand = get_two_operands()
    if second_operand == 0:
        print("Can't divide by 0!")
        return
    print_result(first_operand / second_operand)


def power():
    """ Calculates first number to the power of second number. """
    print("POWER")
    first_operand, second_operand = get_two_operands()
    print_result(first_operand ** second_operand)


def main():
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


if __name__ == "__main__":
    main()
