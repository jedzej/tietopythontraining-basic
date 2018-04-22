#!/usr/bin/env python3

"""
table_printer.py: a practice project "Table Printer" from:
https://automatetheboringstuff.com/chapter6/
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


def print_table(table_data):
    """
    This function  prints the content of the input parameter as well organised
    table
    :param table_data: list of lists of strings
    """
    cols_cnt = len(table_data)
    margin_len = 2

    for i in range(cols_cnt):
        col_width = max([len(x) for x in table_data[i]]) + margin_len
        table_data[i] = [word.rjust(col_width) for word in table_data[i]]

    for i in range(len(table_data[0])):
        for j in range(cols_cnt):
            print(table_data[j][i], sep='', end='')
        print()


def main():

    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]

    print_table(table_data)


if __name__ == '__main__':
    main()
