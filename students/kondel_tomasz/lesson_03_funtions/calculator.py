def print_help_desc():
    """Description"""
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def type_operand():
    """Reading 2 values"""
    while True:
        try:
            print("Input 1st operand:")
            op1 = int(input())
            print("Input 2nd operand:")
            op2 = int(input())
            print("Result:")
            break
        except ValueError:
                print('Please type correct value')

    return op1, op2


def adding():
    """Adding 2 values"""
    print("ADDING")
    op1, op2 = type_operand()
    print(op1 + op2)


def substract():
    """Subtracting 2 values"""
    print("SUBTRACT")
    op1, op2 = type_operand()
    print(op1 - op2)


def multiply():
    """Multiplying 2 values"""
    print("MULTIPLY")
    op1, op2 = type_operand()
    print(op1 * op2)


def divide():
    """Dividing 2 values"""
    print("DIVIDE")
    op1, op2 = type_operand()
    print(op1 / op2)


def power():
    """Power operation: op1 ** op2"""
    print("POWER")
    op1, op2 = type_operand()
    print(op1 ** op2)


def calculator():
    print("Welcome to badly organized calculator:")
    print_help_desc()

    while True:
        print("Enter option:")

        option = input()

        if option == "a":
            adding()

        if option == "s":
            substract()

        if option == "m":
            multiply()

        if option == "d":
            divide()

        if option == "p":
            power()

        if option == "h" or option == "?":
            print("HELP")
            print_help_desc()

        if option == "q":
            print("GOOD BYE")
            break


def main():
    calculator()


if __name__ == '__main__':
    main()
