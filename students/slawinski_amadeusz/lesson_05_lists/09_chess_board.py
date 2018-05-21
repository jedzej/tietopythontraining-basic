#!/usr/bin/env python3

readline = input().split()

rows = int(readline[0])
columns = int(readline[1])

chessboard = [['*' if (i + j) % 2 else '.' for i in range(columns)]
              for j in range(rows)]

for i in range(rows):
    print(' '.join(chessboard[i]))
