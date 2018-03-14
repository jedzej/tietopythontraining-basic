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


while True:
    print("\nAvailable options:")
    options()
    option = input("\nChoose one option: ")

    if option == "a":
        print("\nADDING")
        var_1, var_2 = data()
        print("Addition result: {:f}".format(var_1 + var_2))

    if option == "s":
        print("\nSUBTRACT")
        var_1, var_2 = data()
        print("Subtraction result: {:f}".format(var_1 - var_2))

    if option == "m":
        print("\nMULTIPLY")
        var_1, var_2 = data()
        print("Multiplication result: {:f}".format(var_1 * var_2))

    if option == "d":
        print("\nDIVIDE")
        var_1, var_2 = data()
        print("Division result: {:f}".format(var_1 / var_2))

    if option == "p":
        print("\nPOWER")
        var_1, var_2 = data()
        print("The result of exponentiation: {:f}".format(var_1 ** var_2))

    if option == "h" or option == "?":
        print("\nHELP")

    if option == "q":
        break

print("GOOD BYE")
