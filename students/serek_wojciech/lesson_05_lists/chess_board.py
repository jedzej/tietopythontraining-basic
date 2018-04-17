#!/usr/bin/env python3
"""Chess board exercise"""


def fill(x_val, y_val):
    """Return chessboard fill sign for given field"""
    if (x_val + y_val) % 2 == 0:
        return '.'
    return '*'


def main():
    """Main function"""

    rows, columns = [int(i) for i in input().split()]
    chess_board = [[fill(row, col) for col in range(columns)]
                   for row in range(rows)]

    for row in chess_board:
        print(' '.join(row))


if __name__ == '__main__':
    main()
