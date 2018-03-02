# In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard,
# determine whether a bishop can go from the first to the second in one move.

# The program receives as input four numbers from 1 to 8,
# specifying the column and row numbers of the starting square and the column and row numbers of the ending square.
# The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.

# POL: Laufer

ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

if (abs(ax - bx)) == (abs(ay - by)):
    result = 'YES'
else:
    result = 'NO'

print(result)
