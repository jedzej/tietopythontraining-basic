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
            print("This is not the correct value, try again:")


def input_operands(calculations_name, variables_name):
    print(calculations_name if len(variables_name) != 1
          else 'To current value ' + calculations_name)
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


def calculations(options, new_result=None):
    if options == "a":
        operands = ([new_result] + input_operands("ADDING", ["second"])
                    if new_result is not None
                    else input_operands("ADDING", ["first", "second"]))
        value = adding(operands[0], operands[1])
        result(value)
        return value

    elif options == "s":
        operands = ([new_result] + input_operands("SUBTRACT", ["subtrahend"])
                    if new_result is not None
                    else input_operands("ADDING", ["minuend", "subtrahend"]))
        value = subtract(operands[0], operands[1])
        result(value)
        return value

    elif options == "m":
        operands = ([new_result] + input_operands("MULTIPLY", ["multiplier"])
                    if new_result is not None
                    else input_operands("MULTIPLY",
                                        ["multiplicand", "multiplier"]))
        value = multiply(operands[0], operands[1])
        result(value)
        return value

    elif options == "d":
        operands = ([new_result] + input_operands("DIVIDE", ["divider"])
                    if new_result is not None
                    else input_operands("DIVIDE", ["dividend", "divider"]))
        value = divide(operands[0], operands[1])
        result(value)
        return value

    elif options == "p":
        operands = ([new_result] + input_operands("POWER", ["index"])
                    if new_result is not None
                    else input_operands("POWER", ["base", "index"]))
        value = power(operands[0], operands[1])
        result(value)
        return value

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
            resale = calculations(option)
            while True:
                if option == "a" \
                        or option == "s" \
                        or option == "m" \
                        or option == "d" \
                        or option == "p" \
                        or option == "h" \
                        or option == "?":
                    print("Do you want to use the current result?")
                    print("If YES, key - y / If No, any other key")
                    option_two = input()
                    if option_two == "y":
                        print("What are you going to do with - " + str(resale))
                        help()
                        option = input()
                        resale = calculations(option, resale)
                    else:
                        print("Do you really want to delete result")
                        print("If YES, key - y / If No,any other key")
                        option_two = input()
                        if option_two == "y":
                            print("Your current resale will be deleted.")
                            break
                        else:
                            print("What are you do with -" + str(resale))
                            option = input()
                            help()
                            resale = calculations(option, resale)
                else:
                    break


if __name__ == '__main__':
    main()
