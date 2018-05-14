#!/usr/bin/env python3

"""
snakify_lesson_5.py: Solutions for 3 of problems defined in:
Lesson 5. Strings
(https://snakify.org/lessons/strings_str/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def the_number_of_words():
    """
    This function reads a string consisting of words separated by spaces
    and prints how many words it has
    """
    words_cnt = input().count(' ') + 1
    print(words_cnt)


def to_swap_the_two_words():
    """
    This function reads a string consisting of exactly two words separated
    by a space and prints a new string with the first and second word positions
    swapped
    """
    words = input().split()
    print(' '.join(words[::-1]))


def replace_the_substring():
    """
    This function reads a string and replaces in this string all the numbers
    1 by the word one
    """
    # I guess the method string.replace() is supposed not to be used here:
    # modified_str = input().replace('1', 'one')
    modified_str = input().split('1')
    modified_str = 'one'.join(modified_str)
    print(modified_str)


def main():
    the_number_of_words()
    to_swap_the_two_words()
    replace_the_substring()


if __name__ == '__main__':
    main()
