#!/usr/bin/env python3


def filter_list(_list, _range):
    return [int(x) for x in _list if int(x) not in _range]


if __name__ == '__main__':
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)

    filtered = filter_list(list_of_strings, to_filter_range)

    print(filtered)
