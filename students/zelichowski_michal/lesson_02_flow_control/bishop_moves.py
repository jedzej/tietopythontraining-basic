"""In chess, the bishop moves diagonally, any number of squares. Given
two different squares of the chessboard, determine whether a bishop can
go from the first to the second in one move.

The program receives as input four numbers from 1 to 8, specifying the
column and row numbers of the starting square and the column and row
numbers of the ending square. The program should output YES if a Bishop
can go from the first square to the second in one move, or NO otherwise."""

# Read an integer:
a1 = int(input())
a2 = int(input())

b1 = int(input())
b2 = int(input())

# Print a value:
if a2 - a1 == b2 - b1 or a1 + a2 == b1 + b2:
    print('YES')
else:
    print('NO')
