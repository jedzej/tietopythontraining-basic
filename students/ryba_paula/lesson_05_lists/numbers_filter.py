def filter(strings, filter_range):
    return [int(i) for i in strings if int(i) not in filter_range]


def main():
    list_of_strings = [i for i in input("Input list: ").split()]
    to_filter_range = range(int(input("Type filter: ")))

    print(filter(list_of_strings, to_filter_range))

    example_list_of_strings = ['2', '0', '8', '3']
    example_to_filter_range = range(3)

    print(filter(example_list_of_strings, example_to_filter_range))


if __name__ == '__main__':
    main()
