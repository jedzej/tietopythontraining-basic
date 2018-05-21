# Calculator.py
# piotrsta


def help_calc():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def add(x, y):
    print("Result: " + str(x + y))


def subtract(x, y):
    print("Result: " + str(x - y))


def multiply(x, y):
    print("Result: " + str(x * y))


def divide(x, y):
    print("Result: " + str(x / y))


def power(x, y):
    print("Result: " + str(x ** y))


def input_operand1():
    operand1 = int(input("Input 1st operand: "))
    return operand1


def input_operand2():
    operand2 = int(input("Input 2nd operand: "))
    return operand2


def calc():
    while True:
        print("Enter option:")
        option = input()

        if option == "a":
            print("ADDING")
            x = input_operand1()
            y = input_operand2()
            add(x, y)

        elif option == "s":
            print("SUBTRACT")
            x = input_operand1()
            y = input_operand2()
            subtract(x, y)

        elif option == "m":
            print("MULTIPLY")
            x = input_operand1()
            y = input_operand2()
            multiply(x, y)

        elif option == "d":
            print("DIVIDE")
            x = input_operand1()
            y = input_operand2()
            divide(x, y)

        elif option == "p":
            print("POWER")
            x = input_operand1()
            y = input_operand2()
            power(x, y)

        elif option == "h" or option == "?":
            print("HELP")
            help_calc()

        elif option == "q":
            print("GOOD BYE")
            break

        else:
            print('Wrong option. Try again: ')
            help_calc()


if __name__ == '__main__':
    print("Welcome to NEW calculator:")
    help_calc()
    calc()
