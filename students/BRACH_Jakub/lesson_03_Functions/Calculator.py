def SplashScreen():
    print("{C} Boogie Soft inc. 2018 Welcome to badly organized calculator:")
    ShowHelp()


def RunAdd():
    print("ADDING")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 + add_var_2)


def RubSub():
    print("SUBTRACT")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 - add_var_2)


def RunMul():
    print("MULTIPLY")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 * add_var_2)


def RunDiv():
    print("DIVIDE")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 / add_var_2)


def RunPow():
    print("POWER")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 ** add_var_2)


def ShowHelp():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


SplashScreen()
while True:
    print("Enter option:")

    option = input()

    if option == "a":
        RunAdd()

    if option == "s":
        RunSub()

    if option == "m":
        RunMul()

    if option == "d":
        RunDiv()

    if option == "p":
        RunPow()

    if option == "h" or option == "?":
        ShowHelp()

    if option == "q":
        print("GOOD BYE")
        break
