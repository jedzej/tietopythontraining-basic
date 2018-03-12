#!/usr/bin/env python3

"""
Snakify_L4.py: Solutions for the last 5 problems defined in:
Lesson 4.For loop with range (https://snakify.org/lessons/for_loop_range/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def factorial():
    """
    This function reads a number and computes its factorial
    """
    print("Problem: Factorial")

    number = int(input())
    result = 1

    for n in range(2, number+1):
        result *= n

    print(result)


def the_number_of_zeros():
    """
    This function reads count of numbers followed by the numbers. Then prints the count of zeros among the read numbers
    """
    print("Problem: The number of zeros")

    result = 0
    numbers_count = int(input())

    for i in range(numbers_count):
        number = int(input())
        if not number:
            result += 1

    print(result)


def adding_factorials():
    """
    This function reads an integer n, and prints the sum 1!+2!+3!+...+n!.
    """
    print("Problem: Adding factorials")

    result = 0
    input_number = int(input())

    for i in range(input_number+1, 1, -1):
        result = i*result + 1

    print(result)


def ladder():
    """
    This function reads integer n ≤ 9 and prints a ladder of n steps. The k-th step consists of the integers
    from 1 to k without spaces between them.
    """
    print("Problem: Ladder")

    num = int(input())
    for i in range(1, num+1):
        for k in range(1, i+1):
            print(k, sep="", end="")
        if i < num:
            print("")


def lost_card():
    """
    There was a set of cards with numbers from 1 to N. One of the card is now lost.
    This function reads a number N, followed by N − 1 integers - representing the numbers on the remaining cards
    and prints the number on the lost card.
    """
    print("Problem: Lost card")

    cards_count = int(input())
    actual_sum = 0
    total_sum = 0

    for i in range(1, cards_count):
        actual_sum += int(input())
        total_sum += i

    total_sum += cards_count
    result = total_sum - actual_sum

    print(result)


def main():
    factorial()
    the_number_of_zeros()
    adding_factorials()
    ladder()
    lost_card()


if __name__ == '__main__':
    main()
