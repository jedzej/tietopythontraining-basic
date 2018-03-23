def menu():
    return """
    a - add
    s - subtract
    m - multiply
    d - divide
    p - power
    h,? - help
    q - QUIT
    """


def get_values():
    print("Input 1st operand:")
    var_1 = int(input())
    print("Input 2nd operand:")
    var_2 = int(input())
    print("Result:")
    return [var_1, var_2]


print("Welcome to badly organized calculator:")
option = ''
print(menu())

while option != 'q':

    print("Enter option:")
    option = input()

    if option == "a":
        print("ADDING")
        var_1, var_2 = get_values()
        print(var_1 + var_2)

    if option == "s":
        print("SUBTRACT")
        var_1, var_2 = get_values()
        print(var_1 - var_2)

    if option == "m":
        print("MULTIPLY")
        var_1, var_2 = get_values()
        print(var_1 * var_2)

    if option == "d":
        print("DIVIDE")
        var_1, var_2 = get_values()
        print(var_1 / var_2)

    if option == "p":
        print("POWER")
        var_1, var_2 = get_values()
        print(var_1 ** var_2)

    if option == "h" or option == "?":
        print("HELP")
        print(menu())

print("GOOD BYE")
