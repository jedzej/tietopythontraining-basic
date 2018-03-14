def show_help():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def perform_addition():
    print("ADDING")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 + add_var_2)


def perform_subtraction():
    print("SUBTRACT")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 - add_var_2)


def perform_multiplication():
    print("MULTIPLY")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 * add_var_2)


def perform_division():
    print("DIVIDE")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 / add_var_2)


def perform_power():
    print("POWER")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 ** add_var_2)


def start_calculator():
    print("Welcome to badly organized calculator:")
    show_help()
    option = None

    while option != "q":
        print("Enter option:")
        option = input()

        if option == "a":
            perform_addition()
        elif option == "s":
            perform_subtraction()
        elif option == "m":
            perform_multiplication()
        elif option == "d":
            perform_division()
        elif option == "p":
            perform_power()
        elif option == "h" or option == "?":
            show_help()
    print("GOOD BYE")


if __name__ == '__main__':
    start_calculator()
