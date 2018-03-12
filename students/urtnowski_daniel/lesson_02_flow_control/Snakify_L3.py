#!/usr/bin/env python3

"""
Snakify_L3.py: Solutions for the last 5 problems defined in:
Lesson 3.Conditions: if, then, else (https://snakify.org/lessons/if_then_else_conditions/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def bishop_moves():
    """
    This function checks if the given next move of bishop in chess is correct
    """
    print("Problem: Bishop moves")

    curr_col = int(input())
    curr_row = int(input())
    next_col = int(input())
    next_row = int(input())
    result = "NO"

    diff_row = abs(next_row - curr_row)
    diff_col = abs(next_col - curr_col)
    if diff_row == diff_col:
        result = "YES"

    print(result)


def queen_move():
    """
    This function checks if the given next move of queen in chess is correct
    """
    print("Problem: Queen move")

    curr_col = int(input())
    curr_row = int(input())
    next_col = int(input())
    next_row = int(input())
    result = "NO"

    if next_col == curr_col or curr_row == next_row:
        result = "YES"
    else:
        diff_row = abs(next_row - curr_row)
        diff_col = abs(next_col - curr_col)
        if diff_row == diff_col:
            result = "YES"

    print(result)


def knight_move():
    """
    This function checks if the given next move of knight in chess is correct
    """
    print("Problem: Knight move")

    curr_col = int(input())
    curr_row = int(input())
    next_col = int(input())
    next_row = int(input())
    result = "NO"

    diff_row = abs(next_row - curr_row)
    diff_col = abs(next_col - curr_col)

    if (diff_row == 1 and diff_col == 2) or (diff_row == 2 and diff_col == 1):
        result = "YES"

    print(result)


def chocolate_bar():
    """
    Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular
    parts by breaking it along a selected straight line on its pattern.
    This function reads three integers: n, m, k and determines whether it is possible to split the chocolate bar
    so that one of the parts will have exactly k squares.
    """
    print("Problem: Chocolate bar")

    n = int(input())
    m = int(input())
    k = int(input())
    result = "NO"

    if k <= m*n and (0 == k%n or 0 == k%m):
        result = "YES"

    print(result)


def leap_year():
    """
    This function reads a year number and checks if the it is a leap year
    """
    print("Problem: Leap year")

    year = int(input())
    result = "COMMON"

    if (0 == year%4 and 0 != year%100) or 0 == year%400:
        result = "LEAP"

    print(result)


def main():
    bishop_moves()
    queen_move()
    knight_move()
    chocolate_bar()
    leap_year()


if __name__ == '__main__':
    main()
