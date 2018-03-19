# Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
# first two - for the first cell, and then the last two - for the second cell.

# Read an integer:
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Print a value:

matrix_black = []
matrix_white = []
for i in range(8):
    for j in range(8):
        if ( ((j%2 == 1) and (i%2 == 1)) or ((j%2 == 0) and (i%2 == 0)) ):
            matrix_black.append((j+1,i+1))
        else:
            matrix_white.append((j + 1, i + 1))
#print(matrix_black)
#print(matrix_white)
if ( ((x1,y1) in matrix_black and (x2,y2) in matrix_black) or ((x1,y1) in matrix_white and (x2,y2) in matrix_white) ):
    print("YES")
else:
    print("NO")