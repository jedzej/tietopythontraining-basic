#!/usr/bin/env python3

"""
snakify_lesson_7.py: Solutions for 3 of problems defined in:
Lesson 7. Lists
(https://snakify.org/lessons/lists/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def greater_than_neighbours():
    """
    This function reads a list of numbers and prints the quantity of elements
    that are greater than both of their neighbors
    """
    print("Problem: Greater than neighbours")

    numbers = [int(a) for a in input().split()]
    counter = 0

    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] < numbers[i] and numbers[i + 1] < numbers[i]:
            counter += 1

    print(counter)


def swap_min_and_max():
    """
    This function reads a list of unique numbers, swaps the minimal and maximal
    elements of this list and prints the resulting list.
    """
    print("Problem: Swap min and max")

    numbers = [int(a) for a in input().split()]
    idx_max = 0
    idx_min = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[idx_max]:
            idx_max = i
        if numbers[i] < numbers[idx_min]:
            idx_min = i

    if idx_max != idx_min:
        numbers[idx_min], numbers[idx_max] = numbers[idx_max], numbers[idx_min]

    stringified_nums = [str(num) for num in numbers]
    print(' '.join(stringified_nums))


def the_bowling_alley():
    """
    This function reads the number of pins and the number of balls to be
    rolled, followed by pairs of numbers (one for each ball rolled).
    The subsequent number pairs represent the start to stop (inclusive)
    positions of the pins that were knocked down with each role. Then it
    prints a sequence of characters representing the pins, where "I" is
    a pin left standing and "." is a pin knocked down.
    """
    print("Problem: The bowling alley")

    pins_num, balls_num = [int(num_str) for num_str in input().split()]
    pins_states = pins_num * ['I']

    for i in range(balls_num):
        start, end = [int(num_str) for num_str in input().split()]
        for k in range(start - 1, end):
            pins_states[k] = '.'
        if 'I' not in pins_states:
            break

    print(''.join(pins_states))


def main():
    greater_than_neighbours()
    swap_min_and_max()
    the_bowling_alley()


if __name__ == '__main__':
    main()
