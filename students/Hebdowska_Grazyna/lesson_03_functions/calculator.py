
def parameter(parameter_number):
    print("Input " + parameter_number + " operand:")
    var = int(input())
    n = var*1
    return n

def operations():
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divade")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

def add(v1, v2):
    print("Result:")
    print(v1 + v2)
        
def substrac(v1, v2):
    print("Result:")
    print(add_var_1 - add_var_2)

def multiply(add_var_1, add_var_2):
    print("Result:")
    print(add_var_1 * add_var_2)

def divaide(add_var_1, add_var_2):
    print("Result:")
    print(add_var_1 / add_var_2)

def power(add_var_1, add_var_2):
    print("Result:")
    print(add_var_1 ** add_var_2)

print("Welcome to calculator:")
operations()

while True:
    print("Enter option:")
    
    option = str(input())

    if option == "a":
        print("ADDING")
        add_var_1 = parameter("1st")
        add_var_2 = parameter("2nd")
        add(add_var_1, add_var_2)

    if option == "s":
        print("SUBTRACT")
        add_var_1 = parameter("1st")
        add_var_2 = parameter("2nd")
        substrac(add_var_1, add_var_2)

    if option == "m":
        print("MULTIPLY")
        add_var_1 = parameter("1st")
        add_var_2 = parameter("2nd")
        multiply(add_var_1, add_var_2)
        
    if option == "d":
        print("DIVAIDE")
        add_var_1 = parameter("1st")
        add_var_2 = parameter("2nd")
        divaide(add_var_1, add_var_2)

    if option == "p":
        print("POwER")
        add_var_1 = parameter("1st")
        add_var_2 = parameter("2nd")
        power(add_var_1, add_var_2)

    if option == "h":
        print("HELP")
        operations()
 
    if option == "?":
        print("HELP")
        operations()

    if option =="q": 
        print("GOOD BYE")
        break

