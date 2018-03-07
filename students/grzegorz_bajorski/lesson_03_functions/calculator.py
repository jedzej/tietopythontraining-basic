def usage():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

def data():
    print("Input 1st operand:")
    var_1 = int(input())
    print("Input 2nd operand:")
    var_2 = int(input())
    print("Result:")
    return (var_1, var_2)

print("Welcome to badly organized calculator:")

while True:
    print("Enter option:")
    usage()
    option = input()

    if option == "a":
        print("ADDING")
        add_var_1, add_var_2 = data()
        print(add_var_1 + add_var_2)

    if option == "s":
        print("SUBTRACT")
        add_var_1, add_var_2 = data()
        print(add_var_1 - add_var_2)

    if option == "m":
        print("MULTIPLY")
        add_var_1, add_var_2 = data()
        print(add_var_1 * add_var_2)

    if option == "d":
        add_var_1, add_var_2 = data()
        print(add_var_1 / add_var_2)

    if option == "p":
        print("POWER")
        add_var_1, add_var_2 = data()
        print(add_var_1 ** add_var_2)

    if option == "h":
        print("HELP")
        usage()

    if option == "?":
        print("HELP")
        usage()

    if option == "q":
        break

print("GOOD BYE")
