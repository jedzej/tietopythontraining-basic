def display_options():
    print("Welcome to badly organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")




while True:
    display_options()
    print("Enter option:")

    option = input()


    if option == "a":
        print("ADDING")
        add_var_1 = int(input("Enter first value: "))
        add_var_2 = int(input("Enter second value: "))
        print(add_var_1 + add_var_2)

    if option == "s":
        print("SUBTRACT")
        add_var_1 = int(input("Enter first value: "))
        add_var_2 = int(input("Enter second value: "))
        print(add_var_1 - add_var_2)

    if option == "m":
        print("MULTIPLY")
        add_var_1 = int(input("Enter first value: "))
        add_var_2 = int(input("Enter second value: "))
        print(add_var_1 * add_var_2)

    if option == "d":
        print("DIVIDE")
        add_var_1 = int(input("Enter first value: "))
        add_var_2 = int(input("Enter second value: "))
        print(add_var_1 / add_var_2)

    if option == "p":
        print("POWER")
        add_var_1 = int(input("Enter first value: "))
        add_var_2 = int(input("Enter second value: "))
        print(add_var_1 ** add_var_2)

    if option == "h" or option == "?":
        print("HELP")
        print("a - add")
        print("s - subtract")
        print("m - multiply")
        print("d - divide")
        print("p - power")
        print("h,? - help")
        print("q - QUIT")

    if option == "q":
        print("GOOD BYE")
        break
