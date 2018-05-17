#!/usr/bin/env python3

"""
snakify_lesson_10.py: Solutions for 3 of problems defined in:
Lesson 10. Sets
(https://snakify.org/lessons/sets/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def read_set_of_integers(items_count):
    new_set = set()

    for i in range(items_count):
        new_set.add(int(input()))

    return new_set


def print_set(input_set):
    ordered = list(input_set)

    ordered.sort()
    ordered_len = len(ordered)
    print(ordered_len)
    if ordered_len == 0:
        print('')
    else:
        [print(num) for num in ordered]


def cubes():
    alice_count, bob_count = [int(i) for i in input().split()]

    alice_set = read_set_of_integers(alice_count)
    bob_set = read_set_of_integers(bob_count)

    # common colors
    print_set(alice_set & bob_set)

    # Alice's unique colors
    print_set(alice_set - bob_set)

    # Bob's unique colors
    print_set(bob_set - alice_set)


def the_number_of_distinct_words_in_some_text():
    lines_cnt = int(input())
    words = set()

    for i in range(lines_cnt):
        words |= set(input().split())

    print(len(words))


def guess_the_number():
    n = int(input())
    numbers = set(range(n))
    input_string = str(input())

    while input_string != 'HELP':
        tries = set([int(num) for num in input_string.split(' ')])
        input_string = str(input())
        if input_string == 'YES':
            numbers &= tries
        elif input_string == 'NO':
            numbers -= tries
        else:
            break
        input_string = str(input())

    numbers = list(numbers)
    numbers.sort()
    print(' '.join([str(num) for num in numbers]))


def main():
    cubes()
    the_number_of_distinct_words_in_some_text()
    guess_the_number()


if __name__ == '__main__':
    main()
