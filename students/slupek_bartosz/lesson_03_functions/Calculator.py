def multiply():
    print("MULTIPLY")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 * add_var_2)


def add():
    print("ADDING")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 + add_var_2)


def subtract():
    print("SUBTRACT")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 - add_var_2)


def divide():
    print("DIVIDE")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 / add_var_2)


def power():
    print("POWER")
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
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
