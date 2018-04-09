def display_options():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def add():
    print("ADDING")
    print("Result: " + str(int(input("Input 1st operand:")) +
                           int(input("Input 2nd operand:"))))


def substract():
    print("SUBTRACT")
    print("Result: " + str(int(input("Input 1st operand:")) -
                           int(input("Input 2nd operand:"))))


def multiply():
    print("MULTIPLY")
    print("Result: " + str(int(input("Input 1st operand:")) *
                           int(input("Input 2nd operand:"))))


def divide():
    print("DIVIDE")
    print("Result: " + str(int(input("Input 1st operand:")) /
                           int(input("Input 2nd operand:"))))


def power():
    print("POWER")
    print("Result: " + str(int(input("Input 1st operand:")) **
                           int(input("Input 2nd operand:"))))


if __name__ == "__main__":
    print("Welcome to better organized calculator:")
    display_options()
    option = input("Enter option:")
    while option != "q":
        if option == "a":
            add()
        if option == "s":
            substract()
        if option == "m":
            multiply()
        if option == "d":
            divide()
        if option == "p":
            power()
        if option == "h":
            print("HELP")
            display_options()
        if option == "?":
            print("HELP")
            display_options()
        option = input("Enter option:")
    print("GOOD BYE")
