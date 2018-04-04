def adding(add_var_1, add_var_2):
    res = add_var_1 + add_var_2
    return res


def subtract(add_var_1, add_var_2):
    res = add_var_1 - add_var_2
    return res


def multiply(add_var_1, add_var_2):
    res = add_var_1 * add_var_2
    return res


def divide(add_var_1, add_var_2):
    res = add_var_1 / add_var_2
    return res


def power(add_var_1, add_var_2):
    res = add_var_1 ** add_var_2
    return res


def help_function():
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def main():
    print("Welcome to badly organized calculator:")
    help_function()
    while True:
        print("Enter option:")
        option = input()

        if option == "q":
            print("GOOD BYE")
            break
        elif option == "h" or option == "?":
            help_function()

        else:
            if option != 'a' and option != 's' and option != 'm' and option != 'd' and option != 'p':
                print("Wrong choice, choose another option.")
                continue

            print("Input 1st operand:")
            add_var_1 = int(input())
            print("Input 2nd operand:")
            add_var_2 = int(input())
            result = 0

            if option == "a":
                print("ADDING")
                result = adding(add_var_1, add_var_2)

            elif option == "s":
                print("SUBTRACT")
                result = subtract(add_var_1, add_var_2)

            elif option == "m":
                print("MULTIPLY")
                result = multiply(add_var_1, add_var_2)

            elif option == "d":
                print("DIVIDE")
                result = divide(add_var_1, add_var_2)

            elif option == "p":
                print("POWER")
                result = power(add_var_1, add_var_2)

            print("Result:", result)


if __name__ == '__main__':
    main()
