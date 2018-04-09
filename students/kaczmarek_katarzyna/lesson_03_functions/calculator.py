def input_variables():
    while True:
        try:
            variable1 = float(input("Type first number: "))
            variable2 = float(input("Type second number: "))
            return variable1, variable2
        except ValueError:
            print("Wrong value! Try again!")


def add():
    variable1, variable2 = input_variables()
    print("Operation: ADD. Result: ", variable1 + variable2)


def subtract():
    variable1, variable2 = input_variables()
    print("Operation: SUBTRACT. Result: ", variable1 - variable2)


def multiply():
    variable1, variable2 = input_variables()
    print("Operation: MULTIPLY. Result: ", variable1 * variable2)


def divide():
    try:
        variable1, variable2 = input_variables()
        print("Operation: DIVIDE. Result: ", variable1 / variable2)
    except ZeroDivisionError:
        print("A second argument of a division can't be zero. Try again.")


def power():
    variable1, variable2 = input_variables()
    print("Operation: POWER - Result: ", variable1 ** variable2)


def print_help():
    print("Available options:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def main():
    print("Welcome to the calculator.")
    print_help()

    while True:
        option = input("Enter option: ")

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
            print("Wrong option. Try again.")


if __name__ == '__main__':
    # `python calculator.py` will run main(), `import calculator` will not
    main()
