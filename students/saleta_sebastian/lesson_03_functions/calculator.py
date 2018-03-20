import sys


def input_values():
    print("Input 1st operand: ")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    return add_var_1, add_var_2


def add():
    print("ADDING")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 + add_var_2)


def subtract():
    print("SUBTRACT")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 - add_var_2)


def multiply():
    print("MULTIPLY")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 * add_var_2)


def divide():
    print("DIVIDE")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 / add_var_2)


def power():
    print("POWER")
    add_var_1, add_var_2 = input_values()
    print("Result:")
    print(add_var_1 ** add_var_2)


def help():
    print("HELP")
    print_options()


def quit():
    print("GOOD BYE")
    sys.exit()


def print_options():
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
    'h': help,
    '?': help,
}


def calculator():
    print_options()
    option = input()
    while option != 'q':
        if option in CALCULATOR_DICT:
            CALCULATOR_DICT[option]()
        else:
            print('Wrong operation try again: ')
        print_options()
        option = input()
    quit()


def welcome_text():
    print("Welcome to a little better badly organized calculator:")


if __name__ == "__main__":
    welcome_text()
    calculator()
