#!/usr/bin/env python3

"""
Snakify_L6.py: Solutions for 2 of problems defined in:
Lesson 6. While loop (https://snakify.org/lessons/while_loop/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def the_second_maximum():
    """
    This function reads a sequence of distinct positive integer numbers ended
    with the number 0. Then it determines the value of the second largest
    element in this sequence. It is guaranteed that the sequence has at least
    two elements.
    """
    print("Problem: The second maximum")

    second_max_num = 0
    max_num = 0
    input_num = int(input())

    while input_num:
        if input_num > max_num:
            second_max_num = max_num
            max_num = input_num
        elif input_num > second_max_num:
            second_max_num = input_num
        input_num = int(input())

    print(second_max_num)


def the_number_of_elements_equal_to_the_maximum():
    """
    This function reads a sequence which consists of integer numbers and ends
    with the number 0. Then it determines how many elements of this sequence
    are equal to its largest element.
    """
    print("Problem: The number of elements equal to the maximum")

    max_num = 0
    count = 0
    input_num = int(input())

    while input_num:
        if input_num > max_num:
            max_num = input_num
            count = 1
        elif input_num == max_num:
            count += 1
        input_num = int(input())

    print(count)


def main():
    the_second_maximum()
    the_number_of_elements_equal_to_the_maximum()


if __name__ == '__main__':
    main()
