def welcome():
    print("Welcome to (badly) better organized calculator:")
    help_me()


def help_me():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def numbers_input():
    print("Input 1st operand:")
    var2 = int(input())
    print("Input 2nd operand:")
    var1 = int(input())
    return var1, var2


def adding(var1, var2):
    return var1 + var2


def multiply(var1, var2):
    return var1 * var2


def divide(var1, var2):
    return var1 / var2


def power(var1, var2):
    return var1 ** var2


welcome()

while True:
    print("Enter option:")
    option = input()
    if option == "a":
        print("ADDING")
        var_1, var_2 = numbers_input()
        print("Result:")
        print(adding(var_1, var_2))

    elif option == "s":
        print("SUBTRACT")
        var_1, var_2 = numbers_input()
        print("Result:")
        print(adding(var_1, var_2))

    elif option == "m":
        print("MULTIPLY")
        var_1, var_2 = numbers_input()
        print("Result:")
        print(multiply(var_1, var_2))

    elif option == "d":
        print("DIVIDE")
        var_1, var_2 = numbers_input()
        print("Result:")
        print(divide(var_1, var_2))

    elif option == "p":
        print("POWER")
        var_1, var_2 = numbers_input()
        print("Result:")
        print(power(var_1, var_2))

    elif option == "h":
        help_me()

    elif option == "?":
        help_me()

    elif option == "q":
        print("GOOD BYE")
        break

    else:
        print("Unrecognized option...")
