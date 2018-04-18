#!/usr/bin/env python3

"""
numbers_filter.py: a practice project "Numbers filter" from:
Lesson 5 - Lists + list comprehensions
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def numbers_filter(list_of_strings, filter_range):
    """
    This function  casts list of strings to list of integers and filters
    numbers within supplied range
    :param list_of_strings: a list of strings with numbers
    :param int filter_range: list of integers
    :returns: list of integers representing numbers from the input matrix,
    without values defined in the filter
    """
    result = [int(x) for x in list_of_strings if int(x) not in filter_range]

    return result


def main():
    """
    This function defines a list of strings with numbers and a filter range,
     passes them to the numbers_filter() function and prints its result
    """
    list_of_strings = ['2', '0', '8', '3']
    filter_range = range(3)

    result = numbers_filter(list_of_strings, filter_range)
    print(result)


if __name__ == '__main__':
    main()
