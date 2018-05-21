#In chess, the bishop moves diagonally, any number of squares. Given two different #squares of the chessboard, determine whether a bishop can go from the first to #the second in one move.
#
#The program receives as input four numbers from 1 to 8, specifying the column and #row numbers of the starting square and the column and row numbers of the ending #square. The program should output YES if a Bishop can go from the first square to #the second in one move, or NO otherwise.

import sys

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

#diagonal moves
if (c1x - c2x) == (c1y - c2y):
    print("YES")
else:
    print("NO") 
