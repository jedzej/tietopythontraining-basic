list_of_numbers = [int(i) for i in input("Type the list of numbers: ").split()]

filter_range = int(input("What is the filter range?"))

print("".join([str(x) for x in list_of_numbers[filter_range:len((list_of_numbers))]]))

