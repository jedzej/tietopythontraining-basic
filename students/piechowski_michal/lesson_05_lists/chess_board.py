#!/usr/bin/env python3

rows, columns = [int(x) for x in input().split()]
table = ['.'] * rows
for row in range(0, rows):
    table[row] = ['.'] * columns

for row in range(0, rows):
    for column in range((row + 1) % 2, columns, 2):
        table[row][column] = '*'

for row in table:
    for column_item in row:
        print(column_item, end=' ')
    print("")
