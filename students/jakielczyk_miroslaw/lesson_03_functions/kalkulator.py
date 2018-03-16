import math

def help_menu():
    """Displays help menu"""
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

def provide_inputs():
    """Get two numbers from user"""
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    return add_var_1, add_var_2
    
def add(inputs):
    """takes two arguments, add them and return result"""
    return inputs[0]+inputs[1]

def substract(inputs):
    """takes two arguments, substract them and return result"""
    return inputs[0]-inputs[1]

def multiply(inputs):
    """takes two arguments, multiply them and return result"""
    return inputs[0]*inputs[1]

def divide(inputs):
    """takes two arguments, divide them and return result"""
    return inputs[0]/inputs[1]

def power(inputs):
    """takes two arguments, calculate exponentiation and return result"""
    return math.pow(inputs[0], inputs[1])

def main():
    """Main entry point of the program"""
    while True:
        help_menu()
        option = input()
        if option == "a":
            print ("Result = ",add(provide_inputs()))
        elif option == "s":
            print ("Result = ",substract(provide_inputs()))
        elif option == "m":
            print ("Result = ",multiply(provide_inputs()))
        elif option == "d":
            print ("Result = ",divide(provide_inputs()))
        elif option == "p":
            print ("Result = ",power(provide_inputs()))        
        elif option == "h" or option == "?":
            pass
        elif option == "q":
            print("GOOD BYE")
            break
        else :
            print ("Enter correct option !!! ")

if __name__ == "__main__":
    main()
