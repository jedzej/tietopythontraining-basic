print("Welcome to the awesome calculator :)")


def options():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h, ? - help")
    print("q - QUIT")


def data():
    var_1 = float(input("Enter the first number: "))
    var_2 = float(input("Enter the second number: "))
    return var_1, var_2


def add():
    print("\nADDING")
    var_1, var_2 = data()
    print("Addition result: {:f}".format(var_1 + var_2))


def subtract():
    print("\nSUBTRACT")
    var_1, var_2 = data()
    print("Subtraction result: {:f}".format(var_1 - var_2))


def multiply():
    print("\nMULTIPLY")
    var_1, var_2 = data()
    print("Multiplication result: {:f}".format(var_1 * var_2))


def divide():
    print("\nDIVIDE")
    var_1, var_2 = data()
    print("Division result: {:f}".format(var_1 / var_2))


def power():
    print("\nPOWER")
    var_1, var_2 = data()
    print("The result of exponentiation: {:f}".format(var_1 ** var_2))


def help():
    print("\nHELP")
    options()


print("\nAvailable options:")
options()

while True:
    option = input("\nChoose one option: ")

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

    if option == "h" or option == "?":
        help()

    if option == "q":
        break

print("GOOD BYE")
