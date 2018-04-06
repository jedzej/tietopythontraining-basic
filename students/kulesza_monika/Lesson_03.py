output = 0
num1 = ""
num2 = ""
choice = ""
num1 = input("Input first operand:\n")
num2 = input("Input second operand:\n")

floatnum1 = float(num1)
floatnum2 = float(num2)

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power (x, y):
    return x ** y

print("Welcome to badly organized calculator:\n"
              "a - add\n"
              "s - subtract\n"
              "m - multiply\n"
              "d - divide\n"
              "p - power\n"
              "h,? - help\n"
              "q - QUIT\n")

choice = input("Enter choice your choice: ")
num1 = int(input("Enter First number:  "))
num2 = int(input("Enter Second number:  "))

if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 's':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 'm':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 'd':
    print(num1, "/", num2, "=", divide(num1, num2))

elif choice == 'p':
    print(num1, "**", num2, "=", power(num1, num2))

elif choice == 'h' or '?':
    print("Welcome to badly organized calculator:\n"
          "a - add\n"
          "s - subtract\n"
          "m - multiply\n"
          "d - divide\n"
          "p - power\n"
          "h,? - help\n"
          "q - QUIT\n")

elif choice == 'q':
    print ("goodbye")
    break

else:
    print("Invalid input")

------------------------------------

def the_lenght_of_the_segment():
    def distance(x1, y1, x2, y2):
        from math import sqrt
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    print(distance(x1, y1, x2, y2))

------------------------------------

def negative_exponent():
    def power(a, n):
        res = 1
        for i in range(abs(n)):
            res *= a
        if n >= 0:
            return res
        else:
            return 1 / res
    print(power(float(input()), int(input())))

------------------------------------

def exponentiation():
    def power(a, n):
        if n == 0:
            return 1
        else:
            return a * power(a, n - 1)
    print(power(float(input()), int(input())))

    ------------------------------------

def fibonacci_numbers():
    n = int(input())
    fib1 = 0
    fib2 = 1
    if n < 1:
        print(0)
    elif n == 1:
        print(1)
    else:
        i = 2
        while i <= n:
            fib2, fib1 = fib1 + fib2, fib2
            i += 1
        print(fib2)