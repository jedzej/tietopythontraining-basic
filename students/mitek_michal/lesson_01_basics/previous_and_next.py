
def print_previous_and_next_integer():

    input_number = int(input("Provide a number "))
    previous_number = input_number - 1
    next_number = input_number + 1

    print("The next number for the number " + str(input_number) + " is " + str(next_number))
    print("The previous number for the number " + str(input_number) + " is " + str(previous_number))


print_previous_and_next_integer()
