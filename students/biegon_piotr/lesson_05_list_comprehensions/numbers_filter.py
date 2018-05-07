def filter_list(int_list, int_range):
    out_list = []
    for x in int_list:
        if x not in int_range:
            out_list.append(x)
    return out_list


if __name__ == '__main__':
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)
    list_of_int = [int(i) for i in list_of_strings]
    filtered_list = filter_list(list_of_int, to_filter_range)
    print(filtered_list)
