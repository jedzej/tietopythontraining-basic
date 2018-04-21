#Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two #cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether #a knight can go from the first cell to the second in one move.
#
#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first #two - for the first cell, and then the last two - for the second cell. The program should output YES if a #knight can go from the first cell to the second in one move, or NO otherwise.
 
print("Enter the first cell:")
print("x:")
c1x = int(input())
if (c1x < 1 ) or (c1x > 8):
    print("Error: number out of range")
    sys.exit()

print("y:")
c1y = int(input())
if (c1y < 1 ) or (c1y > 8):
    print("Error: number out of range")
    sys.exit()


print("Enter the second cell:")
print("x:")
c2x = int(input())
if (c2x < 1 ) or (c2x > 8):
    print("Error: number out of range")
    sys.exit()

print("y:")
c2y = int(input())
if (c2y < 1 ) or (c2y > 8):
    print("Error: number out of range")
    sys.exit()

#possible c2 coordinates on the board:
if \
((c1x + 1) == c2x) and ((c1y + 2) == c2y) or \
((c1x + 2) == c2x) and ((c1y + 1) == c2y) or \
((c1x + 2) == c2x) and ((c1y - 1) == c2y) or \
((c1x + 1) == c2x) and ((c1y - 2) == c2y) or \
((c1x - 1) == c2x) and ((c1y - 2) == c2y) or \
((c1x - 2) == c2x) and ((c1y - 1) == c2y) or \
((c1x - 2) == c2x) and ((c1y + 1) == c2y) or \
((c1x - 1) == c2x) and ((c1y + 2) == c2y):
    print("YES")
else:
    print("NO")


