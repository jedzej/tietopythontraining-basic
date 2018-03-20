# Refactor calculator.py file. Organize code into functions, add proper
# docstrings. Ensure that file is compliant with PEP8.


def get_input():
    """Return two values from input."""
    print("Input 1st operand:")
    add_var_one = int(input())
    print("Input 2nd operand:")
    add_var_two = int(input())
    return add_var_one, add_var_two


def summation():
    """Return the sum of two values."""
    print("ADD")
    var_one, var_two = get_input()
    print_result(var_one + var_two)


def subtraction():
    """Return the difference of two values."""
    print("SUBTRACT")
    var_one, var_two = get_input()
    print_result(var_one - var_two)


def multiplication():
    """Return the product of two values."""
    print("MULTIPLY")
    var_one, var_two = get_input()
    print_result(var_one * var_two)


def division():
    """Return the quotient of two values."""
    print("DIVIDE")
    var_one, var_two = get_input()
    print_result(var_one / var_two)


def power():
    """Return first value raised to second value power."""
    print("POWER")
    var_one, var_two = get_input()
    print_result(var_one ** var_two)


def print_info():
    """Print basic options available in calculator."""
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def print_result(result):
    """Prints the result specified in parameter."""
    print("Result:")
    print(result)


print("Welcome to badly organized calculator:")
print_info()

while True:
    print("Enter option:")

    option = input()

    if option == "a":
        summation()

    elif option == "s":
        subtraction()

    elif option == "m":
        multiplication()

    elif option == "d":
        division()

    elif option == "p":
        power()

    elif option == "h":
        print_info()

    elif option == "?":
        print_info()

    elif option == "q":
        print("GOOD BYE")
        break
    else:
        print("Wrong option letter. Try again.")
