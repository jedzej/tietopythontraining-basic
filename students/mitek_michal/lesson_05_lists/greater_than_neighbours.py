
def calculate_number_of_list_elements_with_greater_neighbours():

    input_list = [int(i) for i in input().split()]
    number_of_elements_having_greater_neighbours = 0

    for i in range(1, len(input_list) - 1):
        if input_list[i - 1] < input_list[i] > input_list[i + 1]:
            number_of_elements_having_greater_neighbours += 1

    print(number_of_elements_having_greater_neighbours)


if __name__ == '__main__':
    calculate_number_of_list_elements_with_greater_neighbours()
