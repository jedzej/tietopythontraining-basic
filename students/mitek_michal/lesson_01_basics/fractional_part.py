
def print_fractional_part():

    number = float(input("Provide a number "))

    fractional_number = str(number - int(number))[1:]

    print(fractional_number)


print_fractional_part()