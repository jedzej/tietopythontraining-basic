# Calculator
def adding(add_var_1, add_var_2):
    return(add_var_1 + add_var_2)


def subtract(add_var_1, add_var_2):
    return (add_var_1 - add_var_2)


def multiply(add_var_1, add_var_2):
    return (add_var_1 * add_var_2)


def divide(add_var_1, add_var_2):
    return (add_var_1 / add_var_2)


def power(add_var_1, add_var_2):
    return (add_var_1 ** add_var_2)


def help():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def get_operands():
    global add_var_1
    global add_var_2
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())


def print_result(result):
    print("Result:")
    print(result)


help()
while True:
    print("Enter option:")

    option = input()

    if option == "a":
        print("ADDING")
        get_operands()
        print_result(adding(add_var_1, add_var_2))

    if option == "s":
        print("SUBTRACT")
        get_operands()
        print_result(subtract(add_var_1, add_var_2))

    if option == "m":
        print("MULTIPLY")
        get_operands()
        print_result(multiply(add_var_1, add_var_2))

    if option == "d":
        print("DIVIDE")
        get_operands()
        print_result(divide(add_var_1, add_var_2))

    if option == "p":
        print("POWER")
        get_operands()
        print_result(power(add_var_1, add_var_2))

    if option == "h":
        help()

    if option == "?":
        help()

    if option == "q":
        print("GOOD BYE")
        break
