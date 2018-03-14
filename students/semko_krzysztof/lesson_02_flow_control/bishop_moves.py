"""
In chess, the bishop moves diagonally, any number of squares.
Given two different squares of the chessboard, determine
whether a bishop can go from the first to the second in one move.

The program receives as input four numbers from 1 to 8,
specifying the column and row numbers of the starting square and
the column and row numbers of the ending square.
The program should output YES if a Bishop can go from the first square
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
else:
    print("NO")
