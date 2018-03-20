def get_input_values():
    """Get two numbers from user"""
    print("Input 1st operand:")
    value1 = int(input())
    print("Input 2nd operand:")
    value2 = int(input())
    return value1, value2


def print_result(result):
    """Print the result"""
    print("Result:")
    print(result)


def add():
    """Add two numbers and print the result"""
    print("ADDING")
    val1, val2 = get_input_values()
    print_result(val1 + val2)


def subtract():
    """Subtract two numbers and print the result"""
    print("SUBTRACT")
    val1, val2 = get_input_values()
    print_result(val1 - val2)


def multiply():
    """Multiply two numbers and print the result"""
    print("MULTIPLY")
    val1, val2 = get_input_values()
    print_result(val1 * val2)


def divide():
    """Divide two numbers and print the result"""
    print("DIVIDE")
    val1, val2 = get_input_values()
    try:
        print_result(val1 / val2)
    except ZeroDivisionError:
        print("Cannot divide by zero!")


def power():
    """Calculate the exponentiation and print the result"""
    print("POWER")
    val1, val2 = get_input_values()
    print_result(val1 ** val2)


def show_help():
    """Print out the help menu"""
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def main():
    """Main entry point of the program"""
    print("Welcome to better organized calculator:")
    show_help()

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

        if option in ["h", "?"]:
            show_help()

        if option == "q":
            print("GOOD BYE")
            break


if __name__ == "__main__":
    main()
