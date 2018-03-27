def adding(addX, addY):
    print("ADDING\nResult: " + str(addX + addY))

def subtract(subX, subY):
    print("SUBTRACT\nResult: " + str(subX - subY))

def multiply(mulX, mulY):
    print("MULTIPLY\nResult: " + str(mulX * mulY))

def divide(divX, divY):
    print("DIVIDE\nResult: " + str(divX / diivY))

def power(powX, powY):
    print("POWER\nResult: " + str(powX ** powY))

def help_calc():
    print("HELP "
          "\na - add"
          "\ns - subtract"
          "\nm - multiply"
          "\nd - divide"
          "\np - power"
          "\nh,? - help"
          "\nq - QUIT")

def bye():
    print("GOOD BYE")

def first_value():
    x = int(input("Input 1st operand:"))
    return x

def second_value():
    y = int(input("Input 1st operand:"))
    return y

print("Welcome to badly organized calculator: ")
help_calc()

while True:
    option = input("Enter option:")

    if option == "a":
        adding(first_value(), second_value())
    elif option == "s":
        subtract(first_value(), second_value())
    elif option == "m":
        multiply(first_value(), second_value())
    elif option == "d":
        divide(first_value(), second_value())
    elif option == "p":
        power(first_value(), second_value())
    elif option == "h":
        help()
    elif option == "?":
        help()
    elif option == "q":
        bye()
        break
    else:
        print("Incorrect operation")
        help_calc()