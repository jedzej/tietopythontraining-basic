print("Welcome to badly organized calculator:")
print("a - add")
print("s - subtract")
print("m - multiply")
print("d - divide")
print("p - power")
print("h,? - help")
print("q - QUIT")

while True:
    print("Enter option:")

    option = input()

    if option == "a":
        print("ADDING")
        print("Input 1st operand:")
        add_var_1 = int(input())
        print("Input 2nd operand:")
        add_var_2 = int(input())
        print("Result:")
        print(add_var_1 + add_var_2)

    if option == "s":
        print("SUBTRACT")
        print("Input 1st operand:")
        add_var_1 = int(input())
        print("Input 2nd operand:")
        add_var_2 = int(input())
        print("Result:")
        print(add_var_1 - add_var_2)

    if option == "m":
        print("MULTIPLY")
        print("Input 1st operand:")
        add_var_1 = int(input())
        print("Input 2nd operand:")
        add_var_2 = int(input())
        print("Result:")
        print(add_var_1 * add_var_2)

    if option == "d":
        print("DIVIDE")
        print("Input 1st operand:")
        add_var_1 = int(input())
        print("Input 2nd operand:")
        add_var_2 = int(input())
        print("Result:")
        print(add_var_1 / add_var_2)

    if option == "p":
        print("POWER")
        print("Input 1st operand:")
        add_var_1 = int(input())
        print("Input 2nd operand:")
        add_var_2 = int(input())
        print("Result:")
        print(add_var_1 ** add_var_2)

    if option == "h":
        print("HELP")
        print("a - add")
        print("s - subtract")
        print("m - multiply")
        print("d - divide")
        print("p - power")
        print("h,? - help")
        print("q - QUIT")

    if option == "?":
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
