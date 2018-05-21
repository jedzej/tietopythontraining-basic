
def swap_min_and_max(input_list):

    min_index = input_list.index(min(input_list))
    max_index = input_list.index(max(input_list))

    min_index_value = input_list[min_index]
    max_index_value = input_list[max_index]

    input_list[min_index], input_list[max_index] = [max_index_value,
                                                    min_index_value]


if __name__ == '__main__':
    swap_min_and_max([3, 4, 5, 2, 1])
