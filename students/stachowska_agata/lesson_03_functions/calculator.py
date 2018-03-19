def add(x, y):
    return x + y


def subtrack(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


def input_operand():
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    return add_var_1, add_var_2


def help():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


print("Welcome to great organized calculator:")
help()

while True:
    print("Enter option:")
    option = input()

    if option == "a":
        print("ADDING")
        var_1, var_2 = input_operand()
        print("Result:")
        print(add(var_1, var_2))

    if option == "s":
        print("SUBTRACT")
        var_1, var_2 = input_operand()
        print("Result:")
        print(subtrack(var_1, var_2))

    if option == "m":
        print("MULTIPLY")
        var_1, var_2 = input_operand()
        print("Result:")
        print(multiply(var_1, var_2))

    if option == "d":
        print("DIVIDE")
        var_1, var_2 = input_operand()
        print("Result:")
        print(divide(var_1, var_2))

    if option == "p":
        print("POWER")
        var_1, var_2 = input_operand()
        print("Result:")
        print(power(var_1, var_2))

    if option == "h" or option == "?":
        print("HELP")
        help()

    if option == "q":
        print("GOOD BYE")
        break
