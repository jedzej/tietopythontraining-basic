# Calculator
def adding(add_var_1, add_var_2):
    return(add_var_1 + add_var_2)


def subtract(sub_var_1, sub_var_2):
    return (sub_var_1 - sub_var_2)


def multiply(mlt_var_1, mlt_var_2):
    return (mlt_var_1 * mlt_var_2)


def divide(div_var_1, div_var_2):
    return (div_var_1 / div_var_2)


def power(pow_var_1, pow_var_2):
    return (pow_var_1 ** pow_var_2)


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
    print("Input 1st operand:")
    x = int(input())
    print("Input 2nd operand:")
    y = int(input())
    return (x, y)


def print_result(result):
    print("Result:")
    print(result)


help()
while True:
    print("Enter option:")

    option = input()

    if option == "a":
        print("ADDING")
        add_var_1, add_var_2 = get_operands()
        print_result(adding(add_var_1, add_var_2))

    if option == "s":
        print("SUBTRACT")
        sub_var_1, sub_var_2 = get_operands()
        print_result(subtract(sub_var_1, sub_var_2))

    if option == "m":
        print("MULTIPLY")
        mlt_var_1, mlt_var_2 = get_operands()
        print_result(multiply(mlt_var_1, mlt_var_2))

    if option == "d":
        print("DIVIDE")
        div_var_1, div_var_2 = get_operands()
        print_result(divide(div_var_1, div_var_2))

    if option == "p":
        print("POWER")
        pow_var_1, pow_var_2 = get_operands()
        print_result(power(pow_var_1, pow_var_2))

    if option == "h":
        help()

    if option == "?":
        help()

    if option == "q":
        print("GOOD BYE")
        break
