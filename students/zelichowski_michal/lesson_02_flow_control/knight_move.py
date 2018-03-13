"""Chess knight moves like the letter L. It can move two cells horizontally
and one cell vertically, or two cellsvertically and one cells horizontally.
Given two different cells of the chessboard, determine whether a knight can
go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying
the column and row number, first two -for the first cell, and then the last
two - for the second cell. The program should output YES if a knight can go
from the first cell to the second in one move, or NO otherwise. """

# Read an integer:

a1 = int(input())
a2 = int(input())

b1 = int(input())
b2 = int(input())

# Print a value:
if b1 == a1 - 2 and (b2 == a1 + 1 or b2 == a2 - 1):
    print('YES')
elif b1 == a1 - 1 and (b2 == a2 + 2 or b2 == a2 - 2):
    print('YES')
elif b1 == a1 + 1 and (b2 == a2 + 2 or b2 == a2 - 2):
    print('YES')
elif b1 == a1 + 2 and (b2 == a2 + 1 or b2 == a2 - 1):
    print('YES')

else:
    print('NO')
