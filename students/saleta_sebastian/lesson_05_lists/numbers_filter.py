def filter_numbers(list_of_num, filter_range):
    filter_list = []

    for x in range(len(list_of_num)):
        item = int(list_of_num[x])
        if item not in filter_range:
            filter_list.append(item)
    return filter_list


def main():
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)
    print(filter_numbers(list_of_strings, to_filter_range))


if __name__ == '__main__':
    main()
