
def calculate_factorial():

    number = int(input("Provide a number "))
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print(factorial)


calculate_factorial()
