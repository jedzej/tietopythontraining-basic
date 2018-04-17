def data_input():
    data_in = input().split(" ")
    result = []
    for i in data_in:
        result.append(int(i))
    return result


def chess_board(m, n):
    board = []
    for i in range(m):
        board_row = []
        for j in range(n):
            if i % 2 != j % 2:
                board_row.append("*")
            else:
                board_row.append(".")
        board.append(board_row)
    return board


numbers = data_input()
number_rows = numbers[0]
number_elements = numbers[1]
matrix_board = chess_board(number_rows, number_elements)

for i in range(number_rows):
    print(' '.join(matrix_board[i]))
