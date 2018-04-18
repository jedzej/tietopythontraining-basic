#!/usr/bin/env python3

"""
snakify_lesson_9.py: Solutions for 4 of problems defined in:
Lesson 9. Two-dimensional lists (arrays)
(https://snakify.org/lessons/two_dimensional_lists_arrays/problems/)
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def maximum():
    """
    This function reads two integers representing the rows and columns,
    and subsequent m rows of n elements. Then it prints the index position
    of the maximum element
    """
    print("Problem: Maximum")

    rows, cols = [int(i) for i in input().split()]
    matrix = [[int(j) for j in input().split()] for i in range(rows)]
    max_row_idx = 0
    max_col_idx = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] > matrix[max_row_idx][max_col_idx]:
                max_row_idx, max_col_idx = row, col

    print(max_row_idx, max_col_idx)


def chess_board():
    """
    This function reads two numbers n and m and creates a two-dimensional array
    of size (n×m) and populates it with the characters "." and "*" in
    a checkerboard pattern.
    """
    print("Problem: Chess board")

    rows, cols = [int(i) for i in input().split()]
    matrix = [['.' if (x + y) % 2 == 0 else '*' for y in range(cols)]
              for x in range(rows)]

    for row in matrix:
        print(' '.join(row))


def swap_columns(matrix, i, j):
    """
    This function takes 2-dimentional matrix and two column indexes,
    and swaps the columns with the indexes given
    :param matrix: a list of lists of integers
    :param int i: index of first column to be swapped
    :param int j: index of the second column to be swapped
    :returns: None
    """
    for row in matrix:
        row[i], row[j] = row[j], row[i]


def swap_the_columns_problem():
    """
    This function reads two positive integers m and n, m lines of n elements,
    giving an m×n matrix A, followed by two non-negative integers i and j
    less than n. Then it swaps columns i and j of A and prints the result.
    """
    print("Problem: Swap the columns")

    rows, cols = [int(i) for i in input().split()]
    matrix = [[int(j) for j in input().split()] for i in range(rows)]
    i, j = [int(i) for i in input().split()]

    swap_columns(matrix, i, j)

    for row in matrix:
        print(' '.join([str(num) for num in row]))


def the_diagonal_parallel_to_the_main():
    """
    This function reads an integer n. Then it produces a two-dimensional array
    of size (n×n) and completes it according to the following rules:
    - on the main diagonal writes 0,
    - on the diagonals adjacent to the main, writes 1,
    - on the next adjacent diagonals writes 2 and so forth.
    Next, the function prints the elements of the resulting array with a single
    space between characters.
    """
    print("Problem: The diagonal parallel to the main")

    dim = int(input())
    matrix = [[x for x in range(i, 0, -1)] + [0] +
              [y for y in range(1, dim - i)] for i in range(dim)]

    for row in matrix:
        print(' '.join([str(num) for num in row]))


def main():
    maximum()
    chess_board()
    swap_the_columns_problem()
    the_diagonal_parallel_to_the_main()


if __name__ == '__main__':
    main()
