# Chess knight moves like the letter L. It can move two cells horizontally
# and one cell vertically, or two cells vertically and one cells
# horizontally. Given two different cells of the chessboard, determine
# whether a knight can go from the first cell to the second in one move.

from math import fabs

print("Enter starting column")
column_start = int(input())

print("Enter starting row")
row_start = int(input())

print("Enter destination column")
column_dest = int(input())

print("Enter destination row")
row_dest = int(input())

if (abs(column_start - column_dest) == 2 and abs(row_start - row_dest) == 1) or \
        (abs(column_start - column_dest) == 1 and 2 == abs(row_start - row_dest)):
    print('YES')
else:
    print("NO")
