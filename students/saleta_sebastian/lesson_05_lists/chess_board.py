def create_chess_board(width, height):
    board = []

    for i in range(width):
        board.append([])

        for j in range(height):
            if (i + j) % 2:
                board[i].append('*')
            else:
                board[i].append('.')

    print(board)
    chess_board_in_str = ''
    for k in range(len(board)):
        chess_board_in_str += ''.join(board[k]) + '\n'
    return chess_board_in_str


def main():
    n = int(input())
    m = int(input())
    print(create_chess_board(n, m))


if __name__ == '__main__':
    main()
