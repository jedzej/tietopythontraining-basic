in_string = "1 2 3 4 5 6 7 8 9 10"


def swap_min_and_max(input_string):
    # convert string to list
    val_list = []
    splitted_sting = input_string.split(' ')
    for item in splitted_sting:
        val_list.append(int(item))
    sorted_list = val_list
    sorted_list.sort()

    min_index = val_list.index(sorted_list[0])
    max_index = val_list.index(sorted_list[-1])

    buffer = val_list[min_index]
    val_list[min_index] = val_list[max_index]
    val_list[max_index] = buffer

    return val_list


x = swap_min_and_max(in_string)
print(x)
