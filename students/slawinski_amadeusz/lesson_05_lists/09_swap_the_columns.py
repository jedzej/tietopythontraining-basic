#!/usr/bin/env python3

readline = input().split()

lines = int(readline[0])
elements = int(readline[1])

matrix = []

for i in range(lines):
    readline = input().split()

    matrix.append(readline)

switch_columns = input().split()
for i in range(len(switch_columns)):
    switch_columns[i] = int(switch_columns[i])

for i in range(lines):
    matrix[i][switch_columns[0]], matrix[i][switch_columns[1]] = \
        matrix[i][switch_columns[1]], matrix[i][switch_columns[0]]

for i in range(lines):
    print(' '.join(matrix[i]))
