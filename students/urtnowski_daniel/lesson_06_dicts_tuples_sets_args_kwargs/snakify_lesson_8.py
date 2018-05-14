#!/usr/bin/env python3

"""
snakify_lesson_8.py: Solutions for 2 of problems defined in:
Lesson 8. Functions and recursion
(https://snakify.org/lessons/functions/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def capitalize(lower_case_word):
    first_char_ascii_value = ord(lower_case_word[0])

    if first_char_ascii_value < ord('a') or first_char_ascii_value > ord('z'):
        return lower_case_word

    diff = ord('a') - ord('A')
    first_letter_modified = chr(first_char_ascii_value - diff)

    return first_letter_modified + lower_case_word[1:]


def uppercase():
    words = input().split(' ')

    for i in range(len(words)):
        words[i] = capitalize(str(words[i]))

    print(' '.join(words))


def reverse_the_sequence():
    number = int(input())

    if number != 0:
        reverse_the_sequence()

    print(number)


def main():
    uppercase()
    reverse_the_sequence()


if __name__ == '__main__':
    main()
