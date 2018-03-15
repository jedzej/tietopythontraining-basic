def main():
    welcome()
    while True:
        print("Provide option: ")
        option = input()
        if option == "a":
            add()
        elif option == "m":
            multiply()
        elif option == "s":
            substract()
        elif option == "d":
            divide()
        elif option == "p":
            power()
        elif option == "?" or option == "h":
            help()
        elif option == "q":
            print("GOOD BYE")
            break
        else:
            print("Option not recognized!")

def getInput():
    """Returns two integers based on user input

    """
    print("Input 1st operand:")
    a = int(input())
    print("Input 2nd operand:")
    b = int(input())
    return a, b

def add():
    """Prints result of two numbers adding based on user input

    """
    print("ADDING")
    a,b = getInput()
    print(a + b)

def multiply():
    """Prints results of two numbers multiplication based on user input

    """
    print("MULTIPLY")
    a,b = getInput()
    print(a*b)

def substract():
    """Prints results of two numbers subtraction based on user input

    """
    print("SUBTRACT")
    a,b = getInput()
    print(a - b)

def divide():
    """Prints results of dividing two numbers based on user input

    """
    print("DIVIDE")
    a,b = getInput()
    print(a/b)

def power():
    """Prints results of exponentiation two numbers based on user input

    """
    print("POWER")
    a,b = getInput()
    print(a**b)

def help():
    """Prints possible options

    """
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

def welcome():
    """Prints welcome message possible options

    """
    print("Welcome to well organized calculator:")
    help()

if __name__ == '__main__':
    main()
