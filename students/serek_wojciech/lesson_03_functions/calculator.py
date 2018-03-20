#!/usr/bin/env python3
"""Refactored version of the calculator"""


def get_input_data():
    """Ask user to enter two numbers"""
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())

    return add_var_1, add_var_2


def show_options(message=''):
    """Show available options"""
    print(message)
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def show_result(result):
    """Show calculation result"""
    print("Result")
    print(result)

def add():
    """Add two numbers"""
    print("ADDING")
    add_var_1, add_var_2 = get_input_data()
    show_result(add_var_1 + add_var_2)


def sub():
    """Subtract two numbers"""
    print("SUBTRACT")
    add_var_1, add_var_2 = get_input_data()
    show_result(add_var_1 - add_var_2)


def mul():
    """Multiply two numbers"""
    print("MULTIPLY")
    add_var_1, add_var_2 = get_input_data()
    show_result(add_var_1 * add_var_2)


def div():
    """Divide two numbers"""
    print("DIVIDE")
    add_var_1, add_var_2 = get_input_data()
    try:
        show_result(add_var_1 / add_var_2)
    except ZeroDivisionError:
        print("Invalid argument. Division by 0 not possible!")


def power():
    """Calculate power of two numbers"""
    print("POWER")
    add_var_1, add_var_2 = get_input_data()
    show_result(add_var_1 ** add_var_2)


def main():
    """Main function"""
    show_options("Welcome to refactored calculator")

    while True:
        print("Enter option:")
        option = input()
        if option == "a":
            add()
        elif option == "s":
            sub()
        elif option == "m":
            mul()
        elif option == "d":
            div()
        elif option == "p":
            power()
        elif option == "?" or option == "h":
            show_options("HELP")
        elif option == "q":
            print("GOOD BYE")
            break


if __name__ == '__main__':
    main()
