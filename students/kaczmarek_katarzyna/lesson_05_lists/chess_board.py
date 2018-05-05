def print_chess_board(rows, columns):
    board = []
    for i in range(rows):
        board.append([])
        for j in range(columns):
            if (i + j) % 2 == 0:
                board[i].append('.')
            else:
                board[i].append('*')

    for row in board:
        print(' '.join(row))


def main():
    rows, columns = [int(i) for i
                     in input("Input rows and columns "
                              "(space separated): ").split()]
    print_chess_board(rows, columns)


if __name__ == '__main__':
    main()
