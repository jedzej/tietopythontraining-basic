
def print_first_number_after_decimal_point():

    number = float(input("Provide a number "))

    fractional_number = str(number - int(number))[1:]

    print(fractional_number[1])


print_first_number_after_decimal_point()
