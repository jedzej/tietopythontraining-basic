#!/usr/bin/env python3

"""
the_collatz_sequence.py: a practice project "The Collatz Sequence" from:
https://automatetheboringstuff.com/chapter3/
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def collatz(number):
    """
    This function checks if the input number is odd or even. Then it computes
    number//2 for even number or (3*number + 1) otherwise. The function
    prints the computed value and returns it.

    :param int number: the input number
    :return int: the computed collatz sequence number computed for the input
    """
    if 0 == number % 2:
        ret_val = number // 2
    else:
        ret_val = 3 * number + 1

    print(ret_val)
    return ret_val


def main():
    """
    This function gets a number from the user and calls the collatz() function
    with it. Then it calls the collatz() function repeatedly with the value
    received from the previous call of the collatz() function. The function
    ends up when it receives value 1 from the collatz() function.
    """
    number = int(input("Enter number: "))

    while True:
        number = collatz(number)
        if 1 == number:
            break


if __name__ == '__main__':
    main()
