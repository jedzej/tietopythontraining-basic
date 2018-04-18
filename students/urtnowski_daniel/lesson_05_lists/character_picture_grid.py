#!/usr/bin/env python3

"""
comma_code.py: a practice project "Character Picture Grid" from:
https://automatetheboringstuff.com/chapter4/
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def print_character_picture(grid):
    """
    This function takes a list of lists representing 2D ASCII image and prints
    it to the standard output
    :param grid: a list of lists where each value in the inner lists is
    a one-character string
    :returns: None
    """
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            print(grid[y][x], end='')
        print("")


def main():
    """
    This function defines a list of lists representing ASCII image and passes
    it to print_character_picture() function.
    """
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    print_character_picture(grid)


if __name__ == '__main__':
    main()
