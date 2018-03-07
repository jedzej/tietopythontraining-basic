# Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically,
# or two cells vertically and one cells horizontally. Given two different cells of the chessboard,
# determine whether a knight can go from the first cell to the second in one move.

# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two -
# for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go
# from the first cell to the second in one move, or NO otherwise.

ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

if abs(ax - bx) == 1 and abs(ay - by) == 2 or abs(ax - bx) == 2 and abs(ay - by) == 1:
    result = 'YES'
else:
    result = 'NO'

print(result)
