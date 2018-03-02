# Chess queen moves horizontally, vertically or diagonally to any number of cells.
# Given two different cells of the chessboard,
# determine whether a queen can go from the first cell to the second in one move.

# The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
# first two - for the first cell, and then the last two - for the second cell.
# The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.

ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

if ((abs(ax - bx)) == (abs(ay - by))) or (ax == bx) or (ay == by):
    result = 'YES'
else:
    result = 'NO'

print(result)
