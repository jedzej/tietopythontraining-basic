#!/usr/bin/env python3

"""
snakify_lesson8.py: Solutions for 4 of problems defined in:
Lesson 8. Functions and recursion
(https://snakify.org/lessons/functions/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"

import math


def distance(x1, y1, x2, y2):
    """
    This function computes distance between two points
    :param float x1: the x coordinate of first point
    :param float y1: the y coordinate of first point
    :param float x2: the x coordinate of second point
    :param float y2: the y coordinate of second point
    :return float: the distance between the points (x1,y1) and (x2,y2)
    """
    return math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))


def the_length_of_the_segment():
    """
    This function reads four real numbers representing cartesian coordinates:
    (x1,y1),(x2,y2). Then it calls distance() function and print its result.
    """
    print("Problem: The length of the segment")

    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    result = distance(x1, y1, x2, y2)
    print(result)


def power(a, n):
    """
    This function raises the input parameter a to n-th power
    :param a: positive float number, base
    :param n: integer number, exponent
    :return float: result of the computation
    """
    result = 1
    exponent_is_negative = n < 0

    n = abs(n)
    while n > 0:
        result *= a
        n -= 1

    if exponent_is_negative is True:
        result = 1/result

    return result


def negative_exponent():
    """
    This function reads a positive real number a and integer n. Then it calls
    power() function with the read parameters and prints its result.
    """
    print("Problem: Negative exponent")

    a = float(input())
    n = int(input())

    result = power(a, n)
    print(result)


def power_v2(a, n):
    """
    This function raises the input parameter a to n-th power, without usage of
    loops and built-in ** operator or math.pow(). It uses recursion
    :param a: positive float number, base
    :param n: non-negative integer number, exponent
    :return float: result of the computation
    """
    if n > 0:
        return a * power_v2(a, n-1)

    return 1


def exponentiation():
    """
    This function reads a positive real number a and integer n. Then it calls
    power2() function with the read parameters and prints its result.
    """
    print("Problem: Exponentiation")

    a = float(input())
    n = int(input())

    result = power_v2(a, n)
    print(result)


def fib(n):
    """
    This function computes the n-th Fibonacci number. It uses recursion
    :param n: non-negative integer number
    :return int: the n-th Fibonacci number
    """
    if n > 1:
        return fib(n-1) + fib(n-2)

    return n


def fibonacci_numbers():
    """
    This function reads a non-negative integer number n, uses it as a parameter
    for function fib() and prints its result.
    """
    print("Problem: Fibonacci numbers")

    n = int(input())

    result = fib(n)
    print(result)


def main():
    the_length_of_the_segment()
    negative_exponent()
    exponentiation()
    fibonacci_numbers()


if __name__ == '__main__':
    main()
