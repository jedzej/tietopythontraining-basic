"""
Chess queen moves horizontally, vertically or diagonally to any number of cells.
Given two different cells of the chessboard, determine whether a queen can go
from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8,
each specifying the column and row number, first two - for the first cell,
and then the last two - for the second cell.
The program should output YES if a queen can go from the first cell
to the second in one move, or NO otherwise.
"""

print("Input starting square coordinate x:")
start_x = int(input())
print("Input starting square coordinate y:")
start_y = int(input())
print("Input destination square coordinate x:")
end_x = int(input())
print("Input destination square coordinate y:")
end_y = int(input())

if abs(end_x - start_x) == abs(end_y - start_y):
    print("YES")
elif end_x == start_x or end_y == start_y:
    print("YES")
else:
    print("NO")
