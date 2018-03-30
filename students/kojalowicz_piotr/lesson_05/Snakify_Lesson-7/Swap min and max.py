def swap_min_and_max(list_value):
    minimum = min(list_value)
    maximum = max(list_value)
    new_list_value = list_value
    position_min = list_value.index(minimum)
    position_max = list_value.index(maximum)
    new_list_value[position_min] = maximum
    new_list_value[position_max] = minimum
    return new_list_value


def list_to_string(list_value):
    string = ''
    for value in list_value:
        string += str(value) + " "
    return string


def main():
    values = input()
    numbers = values.split()
    list_of_number = []
    for value in numbers:
        list_of_number.append(int(value))
    print(list_to_string(swap_min_and_max(list_of_number)))


if __name__ == '__main__':
    main()
