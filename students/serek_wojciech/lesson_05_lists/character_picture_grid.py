#!/usr/bin/env python3
"""Character picture grid exercise"""

GRID = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def main():
    """Main function"""
    for y_values, _ in enumerate(GRID[0]):
        for x_values, _ in enumerate(GRID):
            print(GRID[x_values][y_values], end='')
        print('')


if __name__ == '__main__':
    main()
