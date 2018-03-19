

def adding(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        print('Cannot divide by zero')


def power(first, second):
    return first**second


def help():
    print("HELP")
    print("add() - add")
    print("subtract() - subtract")
    print("multiply() - multiply")
    print("divide() - divide")
    print("power() - power")


print("Input 1st operand:")
add_var_1 = int(input())

print("Input 2nd operand:")
add_var_2 = int(input())


help()
print(adding(add_var_1, add_var_2))
print(subtract(add_var_1, add_var_2))
print(multiply(add_var_1, add_var_2))
print(divide(add_var_1, add_var_2))
print(power(add_var_1, add_var_2))
