
def chess_board():

    rows, columns = [int(i) for i in input().split()]
    board = []

    for i in range(rows):
        board.append([])
        for j in range(columns):
            if (i + j) % 2 == 0:
                board[i].append('.')
            else:
                board[i].append('*')

    print(board)


if __name__ == '__main__':
    chess_board()
