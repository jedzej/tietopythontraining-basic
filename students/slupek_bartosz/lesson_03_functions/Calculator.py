def input_operands:
    operand1 = int(input("Input 1st operand: "))
    operand2 = int(input("Input 2nd operand: "))
    print("Result: ")
    return operand1, operand2


def multiply():
    print("MULTIPLY")
    var1, var2 = input_operands()
    print(var1 * var2)


def add():
    print("ADDING")
    var1, var2 = input_operands()
    print(var1 + var2)


def subtract():
    print("SUBTRACT")
    var1, var2 = input_operands()
    print(var1 - var2)


def divide():
    print("DIVIDE")
    var1, var2 = input_operands()
    print(var1 / var2)


def power():
    print("POWER")
    var1, var2 = input_operands()
    print(var1 ** var2)


def help():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def quit():
    print("GOOD BYE")


print("Welcome to badly organized calculator:")
help()

while True:
    option = input('Enter option: ')
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
    elif option == "h" or option == "?":
        help()
    elif option == "q":
        quit()
        break
    else:
        print('Option unknown, please retype or check help "h"')
