#!/usr/bin/env python3
"""Swap columns exercise"""


def swap(matrix, col_1, col_2):
    """Swap given columns in matrix"""
    for row in matrix:
        row[col_1], row[col_2] = row[col_2], row[col_1]


def main():
    """Main function"""

    rows, _ = [int(i) for i in input().split()]
    matrix = [[int(col) for col in input().split()] for row in range(rows)]
    col_1, col_2 = [int(i) for i in input().split()]

    swap(matrix, col_1, col_2)

    for row in matrix:
        print(' '.join([str(el) for el in row]))


if __name__ == '__main__':
    main()
