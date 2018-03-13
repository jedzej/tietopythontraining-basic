#!/usr/bin/env python3

rows, columns = [int(x) for x in input().split()]
table = []

for row in range(0, rows):
    table.append([int(x) for x in input().split()])

maximum_row_number = 0
maximum_column_number = 0
maximum = table[maximum_row_number][maximum_column_number]

for row in range(0, rows):
    for column in range(0, columns):
        if table[row][column] > maximum:
            maximum_row_number = row
            maximum_column_number = column
            maximum = table[maximum_row_number][maximum_column_number]

print(maximum_row_number, end = ' ')
print(maximum_column_number)
