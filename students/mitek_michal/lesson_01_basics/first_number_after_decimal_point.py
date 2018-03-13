
def print_first_number_after_decimal_point():

    number = float(input("Provide a number "))

    fractional_number = int((number - int(number))*10)

    print(fractional_number)


print_first_number_after_decimal_point()
