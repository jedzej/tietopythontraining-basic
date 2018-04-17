# Refactored calculator
# ___________ variable ___________

v1 = 0
v2 = 0
dic = {'a': 'ADDING', 's': 'SUTRACT', 'm': 'MULTIPLY', 'd': 'DIVIDE',
       'p': 'POWER', 'h': 'HELP', '?': 'HELP', 'q': 'GOOD BYE'}


# ___________ functions ___________

def myhelp():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def inputdata():
    global v1, v2, err
    try:
        err = 0
        v1 = int((input("Input 1st operand:")))
        v2 = int((input("Input 2nd operand:")))
        return (v1, v2)
    except ValueError:
        print("It isn't integer!")
        err = 1


def add():
    inputdata()
    return (v1 + v2)


def subtr():
    inputdata()
    return (v1 - v2)


def mltp():
    inputdata()
    return (v1 * v2)


def div():
    inputdata()
    return (v1 / v2)


def power():
    inputdata()
    return (v1 ** v2)


def operation_check(option):
    if (option in dic.keys()) is False:
        print("Missing operation.")
        option = "h"
    print(dic[option])
    if option == "a":
        result = add()
    elif option == "s":
        result = subtr()
    elif option == "m":
        result = mltp()
    elif option == "d":
        result = div()
    elif option == "p":
        result = power()
    elif option == "h" or option == "?":
        result = None
        myhelp()
    else:
        result = None
    if (result is not None) & (err == 0):
        print("Result:", result)


# ___________ program ___________
print("Welcome to badly organized calculator:")
myhelp()
while True:
    option = input("\nEnter option:")
    operation_check(option)
    if option == "q":
        break
