
def print_tens_of_digit():

    number = int(input("Provide a number "))
    print(int(((number % 100)-(number % 10))/10))


print_tens_of_digit()
