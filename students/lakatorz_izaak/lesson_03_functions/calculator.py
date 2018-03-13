# Refactor calculator.py file. Organize code into functions, add proper
# docstrings. Ensure that file is compliant with PEP8.


def get_input():
    """Return two values from input."""
    print("Input 1st operand:")
    add_var_one = int(input())
    print("Input 2nd operand:")
    add_var_two = int(input())
    return add_var_one, add_var_two


def addiction():
    """Return the sum of two values."""
    var_one, var_two = get_input()
    print("Result:")
    print(var_one + var_two)


def substraction():
    """Return the difference of two values."""
    var_one, var_two = get_input()
    print("Result:")
    print(var_one - var_two)


def multiplication():
    """Return the product of two values."""
    var_one, var_two = get_input()
    print("Result:")
    print(var_one * var_two)


def division():
    """Return the quotient of two values."""
    var_one, var_two = get_input()
    print("Result:")
    print(var_one / var_two)


def power():
    """Return first value raised to second value power."""
    var_one, var_two = get_input()
    print("Result:")
    print(var_one ** var_two)


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


print("Welcome to badly organized calculator:")
print_info()

while True:
    print("Enter option:")

    option = input()

    if option == "a":
        print("ADD")
        addiction()

    if option == "s":
        print("SUBTRACT")
        substraction()

    if option == "m":
        print("MULTIPLY")
        multiplication()

    if option == "d":
        print("DIVIDE")
        division()

    if option == "p":
        print("POWER")
        power()

    if option == "h":
        print_info()

    if option == "?":
        print_info()

    if option == "q":
        print("GOOD BYE")
        break
