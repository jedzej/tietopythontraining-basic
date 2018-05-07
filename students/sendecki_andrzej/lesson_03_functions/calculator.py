import sys

def input_operands():
    """input sequence of two operands.

    Gets two integer operands from console  and returns values of theirs.
    To be used in further routines.
    """
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    print("Result:")
    return (add_var_1, add_var_2)        

def add():
    """Addition routine.

    Prints the result of adding two operands.
    Operands are provided by input_operands() function.
    """
    o1, o2 = input_operands()
    print(o1 + o2)

def substract():
    """Substraction routine.

    Prints the result of substracting two operands.
    Operands are provided by input_operands() function.
    """
    o1, o2 = input_operands()
    print(o1 - o2)

def multiply():
    """Multiplication routine

    Prints the result of multiplyng two operands.
    Operands are provided by input_operands() function.
    """
    o1, o2 = input_operands()
    print(o1 * o2)

def divide():
    """Division routine.

    Prints the result of dividing two operands.
    Operands are provided by input_operands() function.
    """
    o1, o2 = input_operands()
    print(o1 / o2)

def power():
    """Exponentiation routine.

    Prints the result of raising operand "o1" to the power of "o2".
    Operands are provided by input_operands() function.
    """
    o1, o2 = input_operands()
    print(o1 ** o2)

def help():
    """ Print help."""    
    print("HELP")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

def quit():
    """Print goodbye message"""
    print("GOOD BYE")

def manage_options(option):
    """Manage options selected by user.

    An input argument is a character representing the action.
    Depending on it a proper routine function is called.
    """
    if (option == "h"):
        help()
    if (option == "a"):
        add()
    if (option == "s"):
        substract()
    if (option == "m"):
        multiply()
    if (option == "d"):
        divide()
    if (option == "p"):
        power()
    if (option == "h" or option == "?"):
        help()
    if (option == "q"):
        quit()

print("Welcome to a better organized calculator:")
help()
option = ""
while (option != "q"):
    print("Enter option:")
    option = input()
    manage_options(option)
