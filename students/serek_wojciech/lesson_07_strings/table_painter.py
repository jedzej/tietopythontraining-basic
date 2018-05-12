#!/usr/bin/env python3
"""Table painter exercise"""


def table_painter(table):
    """Print table"""
    lengths = [0 for _ in range(len(table))]
    for idx, row in enumerate(table):
        for item in row:
            lengths[idx] = max(lengths[idx], len(item))

    for el_in_row in range(len(table[0])):
        print(' '.join(table[row][el_in_row].rjust(lengths[row])
                       for row in range(len(table))))


def main():
    """Main function"""
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]
    table_painter(table_data)


if __name__ == '__main__':
    main()
