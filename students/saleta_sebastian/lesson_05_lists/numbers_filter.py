def filter(list, filter_range):
    filter_list = []

    for x in range(len(list)):
        item = int(list[x])
        if item not in filter_range:
            filter_list.append(item)
    return (filter_list)


def main():
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)
    print(filter(list_of_strings, to_filter_range))


if __name__ == '__main__':
    main()
