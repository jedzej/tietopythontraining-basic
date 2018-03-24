#!/usr/bin/env python3


def print_usage():
    """Prints how to use a calculator."""
    print("Welcome to badly organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def op_add(var_1, var_2):
    """Adds two numbers
 arguments:
    var_1 -- first number
    var_2 -- second number
    """
    return var_1 + var_2


def op_sub(var_1, var_2):
    """Substracts two numbers

    Keyword arguments:
    var_1 -- first number
    var_2 -- second number
    """
    return var_1 - var_2


def op_mul(var_1, var_2):
    """Multiplicates two numbers

    Keyword arguments:
    var_1 -- first number
    var_2 -- second number
    """
    return var_1 * var_2


def op_div(var_1, var_2):
    """Divides two numbers

    Keyword arguments:
    var_1 -- divided number
    var_2 -- dividing number
    """
    return var_1 / var_2


def op_pow(var_1, var_2):
    """Raises a number to power

    Keyword arguments:
    var_1 -- raised number
    var_2 -- power number
    """
    return var_1 ** var_2


def get_numbers():
    """Gets two number from user."""
    while True:
        try:
            print("Input 1st operand:")
            var_1 = int(input())
            print("Input 2nd operand:")
            var_2 = int(input())
            break
        except ValueError:
            print("Try with a number instead!")
    return (var_1, var_2)


def do_operation(operation, var_1, var_2):
    print("Result:")
    print(operation(var_1, var_2))


def main():
    print_usage()

    while True:
        print("Enter option:")

        option = input()

        if option == "a":
            print("ADDING")
            numbers = get_numbers()
            do_operation(op_add, numbers[0], numbers[1])
        elif option == "s":
            print("SUBTRACT")
            numbers = get_numbers()
            do_operation(op_sub, numbers[0], numbers[1])
        elif option == "m":
            print("MULTIPLY")
            numbers = get_numbers()
            do_operation(op_mul, numbers[0], numbers[1])
        elif option == "d":
            print("DIVIDE")
            numbers = get_numbers()
            do_operation(op_div, numbers[0], numbers[1])
        elif option == "p":
            print("POWER")
            numbers = get_numbers()
            do_operation(op_pow, numbers[0], numbers[1])
        elif option == "h" or option == "?":
            print_usage()
        elif option == "q":
            print("GOOD BYE")
            break
        else:
            print("Type 'h' for help!")


if __name__ == '__main__':
    main()
