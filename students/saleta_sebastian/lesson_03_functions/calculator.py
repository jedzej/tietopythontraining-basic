import sys


def input_values():
    """Get two integer values from user"""
    print("Input 1st operand: ")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    return add_var_1, add_var_2


def add():
    """Add two values and print result"""
    print("ADDING")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 + add_var_2)


def subtract():
    """Subtract two values and print result"""
    print("SUBTRACT")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 - add_var_2)


def multiply():
    """Multiply two values and print result"""
    print("MULTIPLY")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 * add_var_2)


def divide():
    """Divide two values and print result"""
    print("DIVIDE")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    try:
        print(add_var_1 / add_var_2)
    except ZeroDivisionError:
        print('Do not divide by zero!')


def power():
    """A function that power the number
        Variables:
            add_var_1: base,
            add_var_2: exponent
        Returns:
            Print result of multiplying n(add_var_2) bases
    """
    print("POWER")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 ** add_var_2)


def calculator_help():
    """A function prints Help string and call print_options() method"""
    print("HELP")
    print_options()


def quit_calculator():
    """A function print Good bye string and call sys.exit()
    application will be closed.
    """
    print("GOOD BYE")
    sys.exit()


def print_options():
    """A function prints available application options"""
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


CALCULATOR_DICT = {
    'a': add,
    's': subtract,
    'm': multiply,
    'd': divide,
    'p': power,
    'h': calculator_help,
    '?': calculator_help,
}


def calculator():
    """Main function"""
    welcome_text()
    print_options()
    option = input()
    while option != 'q':
        if option in CALCULATOR_DICT:
            CALCULATOR_DICT[option]()
        else:
            print('Wrong operation try again: ')
        print_options()
        option = input()
    quit_calculator()


def welcome_text():
    """Function prints welcome message"""
    print("Welcome to a little better badly organized calculator:")


if __name__ == "__main__":
    calculator()
