def get_calculation_name(calculation_type):
    """Get the name for calculation.

    Arguments:
    calculation_type -- the string representing calculation type
    """
    if calculation_type == "a":
        return "ADDING"
    if calculation_type == "s":
        return "SUBTRACT"
    if calculation_type == "m":
        return "MULTIPLY"
    if calculation_type == "d":
        return "DIVIDE"
    if calculation_type == "p":
        return "POWER"


def calculate(calculation_type, arg1, arg2):
    """Perform the specified calculation.

    Arguments:
    calculation_type -- the string representing calculation type
    arg1 -- the first number to use in calculation
    arg2 -- the second number to use in calculation
    """
    if calculation_type == "a":
        return arg1 + arg2
    if calculation_type == "s":
        return arg1 - arg2
    if calculation_type == "m":
        return arg1 * arg2
    if calculation_type == "d":
        return arg1 / arg2
    if calculation_type == "p":
        return arg1 ** arg2


def read_data_and_calculate(calculation_type):
    """Read numbers from user and perform specified calculation.

    Arguments:
    calculation_type -- the string representing calculation type
    """
    print(get_calculation_name(calculation_type))
    print("Input 1st operand:")
    var_1 = int(input())
    print("Input 2nd operand:")
    var_2 = int(input())
    print("Result:")
    print(calculate(calculation_type, var_1, var_2))


def print_help():
    """Print help message."""
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def main():
    print("Welcome to well organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

    while True:
        print("Enter option:")

        option = input()

        if option == "a":
            read_data_and_calculate(option)

        if option == "s":
            read_data_and_calculate(option)

        if option == "m":
            read_data_and_calculate(option)

        if option == "d":
            read_data_and_calculate(option)

        if option == "p":
            read_data_and_calculate(option)

        if option == "h":
            print_help()

        if option == "?":
            print_help()

        if option == "q":
            print("GOOD BYE")
            break


if __name__ == '__main__':
    main()
