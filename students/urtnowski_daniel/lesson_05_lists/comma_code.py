#!/usr/bin/env python3

"""
comma_code.py: a practice project "Comma Code" from:
https://automatetheboringstuff.com/chapter4/
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def comma_code(input_list):
    """
    This function  takes a list value as an argument and returns a string
    with all the items separated by a comma and a space, with 'and'
    inserted before the last item.

    :param input_list: list of ites of any type
    :returns string: stringified input list
    """
    result_str = ""

    if input_list:
        # the input_list is not empty
        for item in input_list[:-1]:
            result_str += "{}, ".format(item)

        result_str += "and {}".format(input_list[-1])

    return result_str


def main():
    """
    This function defines a list of variables of different types, passes it to
    comma_code() function and prints the result.
    """
    heterogeneous_list = ["some string", -589, (-5, [], "another str"), None]

    result = comma_code(heterogeneous_list)
    print(result)


if __name__ == '__main__':
    main()
