
def print_number_ladder():

    number = int(input("Provide number of steps"))

    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


print_number_ladder()
