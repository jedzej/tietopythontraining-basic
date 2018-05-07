#!/usr/bin/env python3
"""Number filters exercise"""


def filter_list(data, limit):
    """ Casts list of strings to list of integers and filters numbers
    within supplied range"""
    return [int(element) for element in data if int(element) not in limit]


def main():
    """Main function"""
    list_of_strings = ['1', '2', '0', '8', '3', '5', '1', '10', '6', '25']
    to_filter_range = range(3)
    print(filter_list(list_of_strings, to_filter_range))


if __name__ == '__main__':
    main()
