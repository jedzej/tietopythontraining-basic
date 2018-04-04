def options():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def get_input():
    print("Input 1st operand:")
    var_1 = int(input())
    print("Input 2nd operand:")
    var_2 = int(input())
    return var_1, var_2


def adding(var_1, var_2):
    print("ADDING")
    return var_1 + var_2


def subtract(var_1, var_2):
    print("SUBTRACT")
    return var_1 - var_2


def multiply(var_1, var_2):
    print("MULTIPLY")
    return var_1 * var_2


def divide(var_1, var_2):
    print("DIVIDE")
    return var_1 / var_2


def power(var_1, var_2):
    print("POWER")
    return var_1 ** var_2


def main():
    print("Welcome to badly organized calculator:")
    options()

    while True:
        print("Enter option:")

        option = input()

        if option == "q":
            print("GOOD BYE")
            break

        elif option == "?" or option == 'h':
            print("HELP")
            options()

        else:
            if option == "a":
                var_1, var_2 = get_input()
                result = adding(var_1, var_2)
            elif option == "s":
                var_1, var_2 = get_input()
                result = subtract(var_1, var_2)
            elif option == "m":
                var_1, var_2 = get_input()
                result = multiply(var_1, var_2)
            elif option == "d":
                var_1, var_2 = get_input()
                result = divide(var_1, var_2)
            elif option == "p":
                var_1, var_2 = get_input()
                result = power(var_1, var_2)
            else:
                print("Wrong option, try again.")
                continue
            print("Result:", result)


if __name__ == '__main__':
    main()
