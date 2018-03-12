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
        print("Input %s operand:" %i)
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


def calculations(options, new_result):
    value = None
    if options == "a":
        if new_result is not None:
            operands = input_operands("To current value ADDING", ["second"])
            result(adding(new_result, operands[0]))
            value = adding(new_result, operands[0])
        else:
            operands = input_operands("ADDING", ["first", "second"])
            result(adding(operands[0], operands[1]))
            value = adding(operands[0], operands[1])
        return value

    elif options == "s":
        if new_result is not None:
            operands = input_operands("To current value SUBTRACT", ["subtrahend"])
            result(subtract(new_result, operands[0]))
            value = subtract(new_result, operands[0])
        else:
            operands = input_operands("SUBTRACT", ["minuend", "subtrahend"])
            result(subtract(operands[0], operands[1]))
            value = subtract(operands[0], operands[1])
        return value

    elif options == "m":
        if new_result is not None:
            operands = input_operands("To current value MULTIPLY", ["multiplier"])
            result(multiply(new_result, operands[0]))
            value = multiply(new_result, operands[0])
        else:
            operands = input_operands("MULTIPLY", ["multiplicand", "multiplier"])
            result(multiply(operands[0], operands[1]))
            value = multiply(operands[0], operands[1])
        return value

    elif options == "d":
        if new_result is not None:
            operands = input_operands("To current value DIVIDE", ["divider"])
            result(divide(new_result, operands[0]))
            value = divide(new_result, operands[0])
        else:
            operands = input_operands("DIVIDE", ["dividend", "divider"])
            result(divide(operands[0], operands[1]))
            value = divide(operands[0], operands[1])
        return value

    elif options == "p":
        if new_result is not None:
            operands = input_operands("To current value POWER", ["index"])
            result(power(new_result, operands[0]))
            value = power(new_result, operands[0])
        else:
            operands = input_operands("POWER", ["base", "index"])
            result(power(operands[0], operands[1]))
            value = power(operands[0], operands[1])
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
            resale = calculations(option, None)
            while True:
                if option == "a" or option == "s" or option == "m" or option == "d" or option == "p" or option == "h" or option == "?":
                    print("Do you want to use the current result for the next calculation?")
                    print("If YES, press the key - y / If No, press any other key")
                    option_two = input()
                    if option_two == "y":
                        print("What are you going to do with - " + str(resale))
                        help()
                        option = input()
                        resale = calculations(option, resale)
                    else:
                        print("Do you really want to delete the current result")
                        print("If YES, press the key - y / If No, press any other key")
                        option_two = input()
                        if option_two == "y":
                            print("Your current resale will be deleted, but the program will continue to work")
                            break
                        else:
                            print("What are you going to do with - " + str(resale))
                            option = input()
                            help()
                            resale = calculations(option, resale)
                else:
                    break

if __name__ == '__main__':
    main()



