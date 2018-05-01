# Refactor calculator.py file.
# Organize code into functions, add proper docstrings.
# Ensure that file is compliant with PEP8.

add_var_1 = 0
add_var_2 = 0


def menu():
    print("Enter option:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def get_operand_1():
    print("Input 1st operand:")
    global add_var_1
    add_var_1 = int(input())
    return add_var_1


def get_operand_2():
    print("Input 2nd operand:")
    global add_var_2
    add_var_2 = int(input())
    return add_var_2


def adding():
    print("ADDING")
    get_operand_1()
    get_operand_2()
    print("Result:")
    print(add_var_1 + add_var_2)


def substrac():
    print("SUBTRACT")
    get_operand_1()
    get_operand_2()
    print("Result:")
    print(add_var_1 - add_var_2)


def multiply():
    print("MULTIPLY")
    get_operand_1()
    get_operand_2()
    print("Result:")
    print(add_var_1 * add_var_2)


def divide():
    print("DIVIDE")
    get_operand_1()
    get_operand_2()
    print("Result:")
    print(add_var_1 / add_var_2)


def power():
    print("POWER")
    get_operand_1()
    get_operand_2()
    print("Result:")
    print(add_var_1 ** add_var_2)


def help():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


while True:
    menu()
    option = input()
    if option == "a":
        adding()

    if option == "s":
        substrac()

    if option == "m":
        multiply()

    if option == "d":
        divide()

    if option == "p":
        power()

    if option == "h" or option == "?":
        help()

    if option == "q":
        print("GOOD BYE")
        break
