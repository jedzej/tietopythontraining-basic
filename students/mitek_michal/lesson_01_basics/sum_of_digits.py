
def print_sum_of_digits():

    number = int(input("Provide a number "))

    list_of_digits = [int(d) for d in str(number)]

    print(sum(list_of_digits))


print_sum_of_digits()
