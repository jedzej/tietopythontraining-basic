def help():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def input_numbers():
    while True:
        try:
            numbers = float(input())
            return numbers
        except NameError:
            print ("This is not the correct value of the variable, try again: ")


def input_operands(calculations_name, variables_name):
    print(calculations_name)
    variables = []
    for i in variables_name:
        print("Input %s operand:" % i)
        variables.append(input_numbers())
    return variables


def result(output):
    print("Result: " + str(output))


def adding(first, second):
    return first + second


def subtract(minuend, subtrahend):
    return minuend - subtrahend


def multiply(multiplicand, multiplier):
    return multiplicand * multiplier


def divide(dividend, divider):
    if divider != 0:
        return dividend / divider
    else:
        print("Divider can not be equal zero!")


def power(base, index):
    return base ** index


def calculations(options):

    if options == "a":
        operands = input_operands("ADDING", ["first", "second"])
        result(adding(operands[0], operands[1]))

    elif options == "s":
        operands = input_operands("SUBTRACT", ["minuend", "subtrahend"])
        result(subtract(operands[0], operands[1]))

    elif options == "m":
        operands = input_operands("MULTIPLY", ["multiplicand", "multiplier"])
        result(multiply(operands[0], operands[1]))

    elif options == "d":
        operands = input_operands("DIVIDE", ["dividend", "divider"])
        result(divide(operands[0], operands[1]))

    elif options == "p":
        operands = input_operands("POWER", ["base", "index"])
        result(power(operands[0], operands[1]))

    elif options == "h" or options == "?":
        print("HELP")
        help()

    else:
        print("There is no such function, try again")
        help()


def main():
    print("Welcome to badly organized calculator:")
    help()
    while True:
        print("Enter option:")
        option = input()
        if option == "q":
            print("GOOD BYE")
            break
        else:
            calculations(option)


if __name__ == '__main__':
    main()
