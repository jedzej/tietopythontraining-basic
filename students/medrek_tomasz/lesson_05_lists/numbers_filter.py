#!/usr/bin/env python3


def numbers_filter(list_of_str, high_pass_filter):
    list_of_num = [int(x) for x in list_of_str if int(x) >= high_pass_filter]
    return list_of_num


def main():
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = 3
    print(numbers_filter(list_of_strings, to_filter_range))


if __name__ == "__main__":
    main()
