def display_help_menu():
    print("Welcome to calculator:")
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def get_text(option):
    if option == "a":
        return "ADDING"
    if option == "s":
        return "SUBTRACT"
    if option == "m":
        return "MULTIPLY"
    if option == "d":
        return "DIVIDE"
    if option == "p":
        return "POWER"


def get_calculation_result(option, var1, var2):
    if option == "a":
        return var1 + var2
    if option == "s":
        return var1 - var2
    if option == "m":
        return var1 * var2
    if option == "d":
        return var1 / var2
    if option == "p":
        return var1 ** var2


def run_calculation(option):
    print(get_text(option))
    print("Input 1st operand:")
    var1 = int(input())
    print("Input 2nd operand:")
    var2 = int(input())
    print("Result:")
    print(get_calculation_result(option, var1, var2))


print("Welcome in calculator.")
while True:
    print("Enter option:")
    option = input()
    if option == "q":
        print("GOODBYE")
        break
    elif option == "h" or option == "?":
        display_help_menu()
    else:
        run_calculation(option)
