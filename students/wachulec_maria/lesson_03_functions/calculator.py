def show_available_options():
    """
    Print available options
    """
    print("Welcome to not-badly organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def take_two_number():
    """
    Input two number and return them
    """
    first_number = int(input("Input 1st operand:\n"))
    second_number = int(input("Input 2st operand:\n"))
    return first_number, second_number


def addition():
    """
    Do add operation between output of
    take_two_number() function
    """
    print("ADDING")
    x1, x2 = take_two_number()
    print("Result: " + str(x1 + x2))


def subtraction():
    """
    Do subtract operation between output of
    take_two_number() function
    """
    print("SUBTRACT")
    x1, x2 = take_two_number()
    print("Result: " + str(x1 - x2))


def multiplication():
    """
    Do multiply operation between output of
    take_two_number() function
    """
    print("MULTIPLY")
    x1, x2 = take_two_number()
    print("Result: " + str(x1 * x2))


def division():
    """
    Do divide operation between output of
    take_two_number() function
    """
    print("DIVIDE")
    x1, x2 = take_two_number()
    print("Result: " + str(x1 / x2))


def exponentiation():
    """
    Do exponent operation between output of
    take_two_number() function
    """
    print("POWER")
    x1, x2 = take_two_number()
    print("Result: " + str(x1 ** x2))


def help_option():
    """
    Run show_available_options()
    """
    print("HELP")
    show_available_options()


def run_calculator():
    """
    Input options from users and do select operation
    """
    show_available_options()
    while True:
        option = input("Enter option:\n")
        if option == 'a':
            addition()
        elif option == 's':
            subtraction()
        elif option == 'm':
            multiplication()
        elif option == 'd':
            division()
        elif option == 'p':
            exponentiation()
        elif option == 'h' or option == '?':
            help_option()
        elif option == 'q':
            print("GOOD BYE")
            break


run_calculator()
