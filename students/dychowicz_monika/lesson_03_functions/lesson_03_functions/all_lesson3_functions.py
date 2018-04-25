def lenght_segment():
    from math import sqrt
    def distance(x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    x1 = float(input("Enter x1:"))
    x2 = float(input("Enter x2:"))
    y1 = float(input("Enter y1:"))
    y2 = float(input("Enter y2:"))
    print(distance(x1, x2, y1, y2))


def negative_exponent():
    def power(a, n):
        result = 1.0
        if n > 0:
            for i in range(n):
                result *= a
        elif n == 0:
            result = 1.0
        else:
            for i in range(abs(n)):
                result *= 1 / a
                return result
            a = float(input("enter number:"))
            n = int(input("enter the exponent:"))
            print(power(a, n))


def exponentation(a, n):
    def power(a, n):
        if n >= 1:
            return a * power(a, n - 1)
        elif n == 0:
            return 1

    print(power(a, n))


def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


def collatz_sequence():
    # Function named. that has one parameter named number.If number is even, then collatz should print
    # number //2 and return this value. If number is odd, then collatz should print and return 3* number +1
    number = int(input("Enter a number:"))
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result


def calc():
    print("Welcome to badly organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")

    while True:
        print("Enter option:")

        option = input()

        if option == "a":
            add()

        if option == "s":
            substract()

        if option == "m":
            multiply()

        if option == "d":
            divide()

        if option == "p":
            power()

        if option == "h":
            help()

        if option == "?":
            help()

        if option == "q":
            quit()


def add():
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    result = a+b
    print(result)


def substract():
    print("SUBTRACT")
    print("Enter a number:")
    add_var_1 = int(input())
    print("Enter a number:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 - add_var_2)


def multiply():
    print("MULTIPLY")
    print("Enter a number:")
    add_var_1 = int(input())
    print("Enter a number:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 * add_var_2)


def divide():
    print("DIVIDE")
    print("Enter a number:")
    add_var_1 = int(input())
    print("Enter a number:")
    add_var_2 = int(input())
    print("Result:")
    print(add_var_1 / add_var_2)


def power():
    print("POWER")


def help():
    print("HELP")


def help():
    print("h,? - help")


def quit():
    print("q - QUIT")
        #break
    print("GOOD BYE")



if __name__ == '__main__':
    # lenght_segment()
    # negative_exponent()
    # a = float(input("enter a number:"))
    # n = int(input("enter the exponent:"))
    # exponentation(a,n)
    # print(exponentation(int(input()), int(input())))
    # print(fib(int(input("enter number: "))))
    # print(collatz_sequence())
    #calc()
# pass
