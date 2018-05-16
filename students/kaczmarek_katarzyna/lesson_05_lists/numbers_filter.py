def filter_by_range(strings, filter_range):
    return [int(i) for i in strings if int(i) not in filter_range]


def main():
    list_of_strings = [i for i in input("Input numbers "
                                        "(space separated): ").split()]
    to_filter_range = range(int(input("Filter range: ")))

    print(filter_by_range(list_of_strings, to_filter_range))


if __name__ == '__main__':
    main()
