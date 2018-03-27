# functions


def help():
    """help
    """
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def inputs(message):
    """data input
    message : str
    """
    print(message)
    var_1 = int(input("Input 1st operand: "))
    var_2 = int(input("Input 2nd operand: "))
    print("Result:")
    return var_1, var_2


def add():
    var_1, var_2 = inputs("ADD")
    print(var_1 + var_2)


def subtract():
    var_1, var_2 = inputs("SUBTRACT")
    print(var_1 - var_2)


def multiply():
    var_1, var_2 = inputs("MULTIPLY")
    print(var_1 * var_2)


def divide():
    var_1, var_2 = inputs("DIVIDE")
    print(var_1 / var_2)


def power():
    var_1, var_2 = inputs("POWER")
    print(var_1 ** var_2)


# program

print("Welcome to well organized calculator:")

help()

while True:
    print("Enter option:")

    option = input()

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
    elif option in {"h", "?"}:
        help()
    elif option == "q":
        print("GOOD BYE")
        break
    else:
        print("No such option. Repeat:")
