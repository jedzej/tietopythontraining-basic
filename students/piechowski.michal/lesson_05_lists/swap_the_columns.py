#!/usr/bin/env python3


def swap_columns(table, first_column, second_column):
    for row in range(0, rows):
        temp = table[row][first_column]
        table[row][first_column] = table[row][second_column]
        table[row][second_column] = temp


rows, columns = [int(x) for x in input().split()]
table = []

for row in range(0, rows):
    table.append([int(x) for x in input().split()])

first_column, second_column = [int(x) for x in input().split()]
swap_columns(table, first_column, second_column)

for row in range(0, rows):
    for column in range(0, columns):
        print(table[row][column], end = ' ')
    print("")
