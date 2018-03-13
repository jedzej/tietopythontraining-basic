"""Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the
chessboard, determine whether a queen can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two -
for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from
the first cell to the second in one move, or NO otherwise. """

# Read an integer:
a1 = int(input())
a2 = int(input())

b1 = int(input())
b2 = int(input())

# Print a value:
if a2 - a1 == b2 - b1 or a1 + a2 == b1 + b2 or a1 == b1 or a2 == b2:
    print('YES')
else:
    print('NO')
