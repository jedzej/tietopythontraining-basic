'''
Given two numbers n and m. Create a two-dimensional array of size
(n×m) and populate it with the characters "." and "*" in a
checkerboard pattern. The top left corner
should have the character "." .
'''


def chess_board():
    n, m = [int(s)
            for s in input("Enter 2 numbers separated with space:").split()]
    board = [[' '] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    board[i][j] = '.'
                else:
                    board[i][j] = '*'
            else:
                if j % 2 != 0:
                    board[i][j] = '.'
                else:
                    board[i][j] = '*'
    for i in range(n):
        print(' '.join(board[i]))


if __name__ == "__main__":
    try:
        chess_board()
    except ValueError:
        print("Invalid input")
