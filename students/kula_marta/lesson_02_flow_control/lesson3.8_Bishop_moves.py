#!/usr/bin/env python

from math import fabs

PATERN_0 = [0, 1, 0, 1, 0, 1, 0, 1]
PATERN_1 = [1, 0, 1, 0, 1, 0, 1, 0]

p1_x = int(input("give 1-x: "))
p1_y = int(input("give 1-y: "))

p2_x = int(input("give 2-x: "))
p2_y = int(input("give 2-y: "))

if ((p1_x > 8) | (p1_x < 1) | (p2_x > 8) | (p2_x < 1)):
    print("Incorect input!")
else:
    # init table
    board = [[0]*8]*8

    for x in range(0, 8):
        if (x % 2) == 0:
            board[x] = PATERN_0
        else:
            board[x] = PATERN_1

    d = fabs(p1_x - p2_x)

    if (p2_y == p1_y + d) | (p2_y == p1_y - d):
        print("YES")
    else:
        print("NO")

# print(board)
