def calculate(option, a, b):
    """
    Performs calculations according to selected option
    :param option: string, one of selected options
    :param a: integer
    :param b: integer
    :return: number
    """
    if option == "a":
        return a + b
    if option == "s":
        return a - b
    if option == "m":
        return a * b
    if option == "d":
        return a / b
    if option == "p":
        return a ** b


def calculator(option):
    """
    Main function displaying info/result/help to user. It also runs calculate
    function if user selects the right option.
    :param option: String - selected option, one of values: a,s,m,d,p,h,?,q
    """
    try:
        if option == "a":
            print("ADDING")
        if option == "s":
            print("SUBSTRACT")
        if option == "m":
            print("MULTIPLY")
        if option == "d":
            print("DIVIDE")
        if option == "p":
            print("POWER")
        if option == "h" or option == "?":
            print(
                "HELP\na - add\ns - subtract\nm - multiply\nd - divide\n"
                "p - power\nh,? - help\nq - QUIT")
        if option == "q":
            print("GOOD BYE")
            exit(0)
        if option_chosen in ("a", "s", "m", "d", "p"):
            var_1 = int(input("Input 1st operand:"))
            var_2 = int(input("Input 2nd operand:"))
            result = calculate(option_chosen, var_1, var_2)
            print("Result: ")
            print(result)
    except ValueError:
        print('Error: Enter one of options: a,s,m,d,p,h,?,q')


print(
    "Welcome to better organized calculator:\na - add\ns - subtract\nm - "
    "multiply\nd - divide\np - power\nh,? - help\nq - QUIT")

while True:
    option_chosen = input("Enter option:")
    calculator(option_chosen)
