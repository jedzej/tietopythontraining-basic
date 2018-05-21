# Program print chess board using . and *

n = int((input("How many rows?: ")))
m = int((input("How many columns?: ")))

chess_board = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if(i % 2 == 0) & (j % 2 == 0):
            chess_board[i][j] = "."
        elif(i % 2 != 0) & (j % 2 != 0):
            chess_board[i][j] = "."
        else:
            chess_board[i][j] = "*"

# print list
for row in chess_board:
    print(' '.join([str(elem) for elem in row]))
