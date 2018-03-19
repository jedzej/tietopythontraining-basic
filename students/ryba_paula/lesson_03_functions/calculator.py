def show_help():
    '''Print calculator options'''
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def input_numbers():
    '''Get input from user'''
    while True:
        try:
            var1 = float(input("Input first number: "))
            var2 = float(input("Input second number: "))
            return var1, var2
        except ValueError:
            print("The value must be a number, try again!")


def addition():
    '''Add two numbers and print the result'''
    var1, var2 = input_numbers()
    print("The result is: ", var1 + var2)


def subtraction():
    '''Subtract two numbers and print the result'''
    var1, var2 = input_numbers()
    print("The result is: ", var1 - var2)


def multiplication():
    '''Multiplication of two numbers and print the result'''
    var1, var2 = input_numbers()
    print("The result is: ", var1 * var2)


def division():
    '''Divide two numbers and print the result'''
    try:
        var1, var2 = input_numbers()
        print("The result is: ", var1 / var2)
    except ZeroDivisionError:
        print("You cannot divide by zero. Try again.")


def power():
    '''Check the exponentiation of two numbers and print the result'''
    var1, var2 = input_numbers()
    print("The result is: ", var1 ** var2)


def main():
    '''Print the welcome message, options, choose an option and print the
    result'''
    print("Welcome to the well-organized calculator.")
    print("Here are the available options:")
    show_help()

    while True:
        option = input("Choose one of the options. ")

        if option == "a":
            addition()

        elif option == "s":
            subtraction()

        elif option == "m":
            multiplication()

        elif option == "d":
            division()

        elif option == "p":
            power()

        elif option == "h" or option == "?":
            show_help()

        elif option == "q":
            print("Bye!")
            break

        else:
            print("No such option. Try again.")


if __name__ == '__main__':
    main()
