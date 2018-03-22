def help():
    print("Available options: ")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def quit_the_program():
    print("GOOD BYE")


def numbers():
    while True:
        print("Input 2 numbers")
        print("First number is: ")
        add_var_1 = int(input())
        print("Second number is: ")
        add_var_2 = int(input())
        return add_var_1, add_var_2


def add():
    add_var_1, add_var_2 = numbers()
    print("Result:")
    print(add_var_1 + add_var_2)


def subtract():
    add_var_1, add_var_2 = numbers()
    print("Result:")
    print(add_var_1 - add_var_2)


def multiply():
    add_var_1, add_var_2 = numbers()
    print("Result:")
    print(add_var_1 * add_var_2)


def divide():
    try:
        add_var_1, add_var_2 = numbers()
        print("Result:")
        print(add_var_1 / add_var_2)
    except ZeroDivisionError:
        print("You can not divide by zero")


def power():
    add_var_1, add_var_2 = numbers()
    print("Result:")
    print(add_var_1 ** add_var_2)


def main():
    print("Welcome to a well-organized calculator!")
    help()
    while True:
        print("Enter option: ")
        option = input()
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
            quit_the_program()
            break
        else:
            print("Enter option again: ")
            continue


if __name__ == "__main__":
    main()
