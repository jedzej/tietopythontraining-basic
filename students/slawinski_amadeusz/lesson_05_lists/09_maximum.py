#!/usr/bin/env python3

readline = input().split()

rows = int(readline[0])
cols = int(readline[1])

array = []

for i in range(rows):
    readline = input().split()

    for j in range(cols):
        readline[j] = int(readline[j])

    array.append(readline)

nmax = []
for i in range(rows):
    nmax.append(max(array[i]))

row = nmax.index(max(nmax))
column = array[row].index(max(nmax))

print(str(row) + ' ' + str(column))
