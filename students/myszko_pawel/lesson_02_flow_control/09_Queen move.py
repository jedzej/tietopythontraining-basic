# Chess queen moves horizontally, vertically or diagonally to any number of cells.
# Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and
# then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.

import math
# Read an integer:
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Print a value:
if( ((x2 == x1) or (y2 == y1)) or (abs(x2 - x1) == abs(y2 - y1)) ):
    print("YES")
else:
    print("NO")