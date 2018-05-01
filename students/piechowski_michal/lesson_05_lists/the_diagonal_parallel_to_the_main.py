#!/usr/bin/env python3

dimention = int(input())
table = [0] * dimention

for row in range(0, dimention):
    table[row] = [0] * dimention
    for column in range(0, dimention):
        table[row][column] = abs(row - column)
        print(table[row][column], end=' ')
    print("")
