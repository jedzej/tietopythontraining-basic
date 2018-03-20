
def get_input():

    while True:
        try:
            print("Input 1st operand:")
            var_1 = int(input())
            print("Input 2nd operand:")
            var_2 = int(input())
            return var_1, var_2
            break
        except:
            print("please enter 2 integers")

def addition():

    add_var_1, add_var_2 = get_input()
    print("Result:")
    print(add_var_1 + add_var_2)

def subtract():

    sub_var_1, sub_var_2 = get_input()
    print("Result:")
    print(sub_var_1 - sub_var_2)

def multiply():

    multi_var_1, multi_var_2 = get_input()
    print("Result:")
    print(multi_var_1 * multi_var_2)

def divide():

    div_var_1, div_var_2 = get_input()
    print("Result:")
    print(div_var_1 / div_var_2)

def power():

    power_var_1, power_var_2 = get_input()
    print("Result:")
    print(power_var_1 ** power_var_2)

def print_options():

    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

print("Welcome to badly organized calculator:")
print_options()

while True:

    print("Enter option:")
    option = input()

    if option == "a":
        print("ADDITION")
        addition()

    elif option == "s":
        print("SUBTRACT")
        subtract()

    elif option == "m":
        print("MULTIPLY")
        multiply()

    elif option == "d":
        print("DIVIDE")
        divide()

    elif option == "p":
        print("POWER")
        power()

    elif option == "h":
        print("HELP")
        print_options()

    elif option == "?":
        print("HELP")
        print_options()

    elif option == "q":
        print("GOOD BYE")
        break

    else:
        print("please select from one of the following options:")
        print_options()

