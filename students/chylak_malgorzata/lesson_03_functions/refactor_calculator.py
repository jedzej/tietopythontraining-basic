def add():
    """Add function docstring"""
    print("ADDING")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 + add_var_2)


def subtract():
    """Subtract function docstring"""
    print("SUBTRACT")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 - add_var_2)


def multiply():
    """Multiply function docstring"""
    print("MULTIPLY")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 * add_var_2)


def divide():
    """Divide function docstring"""
    print("DIVIDE")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 / add_var_2)


def power():
    """Power function docstring"""
    print("POWER")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 ** add_var_2)


def help_func():
    """Help function docstring"""
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def exit_func():
    """Quit function docstring"""
    print("GOOD BYE")


def main():
    while True:

        print("Enter option:")

        option = input()

        if option == "a":
            add()

        if option == "s":
            subtract()

        if option == "m":
            multiply()

        if option == "d":
            divide()

        if option == "p":
            power()

        if option == "h":
            help_func()

        if option == "?":
            help_func()

        if option == "q":
            exit_func()

            break

        else:
            print("Wrong name")


if __name__ == '__main__':
    print("Welcome to badly organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

    main()
