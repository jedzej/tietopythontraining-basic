def input_validation():
    global val
    while True:
        try:
            print('Set real number:')
            val = float(input())
        except ValueError:
            print('ValueError: Incorrect real number!')
            input_validation()
        break
    return val


def add(add_var_1, add_var_2):
    return add_var_1 + add_var_2


def sub(add_var_1, add_var_2):
    return add_var_1 - add_var_2


def mul(add_var_1, add_var_2):
    return add_var_1 * add_var_2


def div(add_var_1, add_var_2):
    try:
        div_val = add_var_1 / add_var_2
    except ZeroDivisionError:
        print('Error: ZeroDivisionError')
        div_val = None
    return div_val


def power(add_var_1, add_var_2):
    return add_var_1 ** add_var_2


def help_menu():
    print("Welcome to good organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def main():
    """Main program function"""
    help_menu()
    while True:
        option = input()
        if option == "a":
            """add operation"""
            p1 = input_validation()
            p2 = input_validation()
            print("Result of addition of two arguments is equal: {0}".format(add(p1, p2)))
        elif option == "s":
            """subtract operation"""
            p1 = input_validation()
            p2 = input_validation()
            print("Result of subtraction of two arguments is equal: {0}".format(sub(p1, p2)))
        elif option == "m":
            """MULTIPLY"""
            p1 = input_validation()
            p2 = input_validation()
            print("Result of multiplication of two arguments is equal: {0}".format(mul(p1, p2)))
            mul(p1, p2)
        elif option == "d":
            """DIVIDE"""
            p1 = input_validation()
            p2 = input_validation()
            print("Result of division of two arguments is equal: {0}".format(div(p1, p2)))
        elif option == "p":
            """POWER"""
            p1 = input_validation()
            p2 = input_validation()
            print("Result of power of two arguments is equal: {0}".format(power(p1, p2)))
        elif option == "h" or option == "?":
            """HELP"""
            help_menu()
        elif option == "q":
            """GOOD BYE"""
            break


if __name__ == "__main__":
    main()
