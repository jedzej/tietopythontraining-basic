"""
Chess knight moves like the letter L. It can move two cells horizontally
and one cell vertically, or two cells vertically and one cells horizontally.
Given two different cells of the chessboard, determine whether a knight
can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8,
each specifying the column and row number, first two - for the first cell,
and then the last two - for the second cell. The program should output
YES if a knight can go from the first cell to the second in one move,
or NO otherwise.
"""

print("Input starting square coordinate x:")
start_x = int(input())
print("Input starting square coordinate y:")
start_y = int(input())
print("Input destination square coordinate x:")
end_x = int(input())
print("Input destination square coordinate y:")
end_y = int(input())

if abs(end_x - start_x) == 2 and abs(end_y - start_y) == 1:
    print("YES")
elif abs(end_y - start_y) == 2 and abs(end_x - start_x) == 1:
    print("YES")
else:
    print("NO")
