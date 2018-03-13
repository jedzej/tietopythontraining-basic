#!/usr/bin/env python3

"""
calculator.py: refactored calculator.py from:
https://github.com/jedzej/tietopythontraining-basic/blob/master/course/\
lesson_03_functions/calculator.py
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def print_info(header_str="Welcome to well organized calculator:"):
    """
    This function prints information for user containing input options
    :param string header_str: Additional information for user printed
    in the first place
    """
    print(header_str)
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def get_operands():
    """
    This function reads two operands from the user
    :return [int, int]: two operands got from user
    """
    print("Input 1st operand:")
    operand_1 = int(input())
    print("Input 2nd operand:")
    operand_2 = int(input())

    return operand_1, operand_2


def add(a, b):
    """
    This function adds the two input operands
    :param int a: first operand
    :param int b: second operand
    :return int: the result of addition of the input parameters
    """
    return a + b


def subtract(a, b):
    """
    This function subtracts the two input operands
    :param int a: first operand
    :param int b: second operand
    :return int: the result of subtraction of the input parameters
    """
    return a - b


def multiply(a, b):
    """
    This function multiplies the two input operands
    :param int a: first operand
    :param int b: second operand
    :return int: the result of multiplication of the input parameters
    """
    return a * b


def divide(a, b):
    """
    This function divides the two input operands
    :param int a: first operand
    :param int b: second operand
    :return int: the result of division of the input parameters
    """
    return a / b


def power(a, b):
    """
    This function performs the exponentiation operation on the two input
    operands
    :param int a: first operand
    :param int b: second operand
    :return int: the value of the first operand raised to the power of
    the second operand
    """
    return a ** b


def perform_operation(operation_str, operation_fun):
    """
    This function prints the name of operation, then reads two operands from
    user and prints result of operation performed on them.
    :param string operation_str: the name of performed operation
    :param operation_fun: function taking two integer parameters and returning
    integer result
    """
    print(operation_str)
    a, b = get_operands()
    result = operation_fun(a, b)
    print("Result:")
    print(result)


def main():
    """
    This function prints menu for user and executes the action chosen
    """
    print_info()

    while True:
        print("Enter option:")
        option = input()

        if option == "a":
            perform_operation("ADDING", add)
        elif option == "s":
            perform_operation("SUBTRACT", subtract)
        elif option == "m":
            perform_operation("MULTIPLY", multiply)
        elif option == "d":
            perform_operation("DIVIDE", divide)
        elif option == "p":
            perform_operation("POWER", power)
        elif option == "h" or option == "?":
            print_info("HELP")
        elif option == "q":
            print("GOOD BYE")
            break


if __name__ == '__main__':
    main()
