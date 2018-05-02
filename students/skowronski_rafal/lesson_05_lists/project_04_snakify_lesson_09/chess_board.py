from helper import print_matrix_as_string


def get_chess_board(rows_count, cols_count):
    matrix = [['.' for col in range(cols_count)] for row in range(rows_count)]

    is_dot = True

    for row in range(rows_count):
        for col in range(cols_count):
            if is_dot is False:
                matrix[row][col] = '*'
            is_dot = not is_dot
        is_dot = True if matrix[row][0] == '*' else False

    return matrix


if __name__ == '__main__':
    rows_count = int(input('Enter number of rows: '))
    cols_count = int(input('Enter number of columns: '))

    matrix = get_chess_board(rows_count, cols_count)
    print_matrix_as_string(matrix)
