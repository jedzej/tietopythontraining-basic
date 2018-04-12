def get_user_input():
    return [int(s) for s in input().split()]


def show_chessboard(rows, columns):
    list_with_chars = \
        ["." if i % 2 == 0 else "*" for i in range(columns)]
    reversed_list_with_chars = \
        ["." if i % 2 != 0 else "*" for i in range(columns)]
    for row_index in range(rows):
        if row_index % 2 == 0:
            print(' '.join(list_with_chars))
        else:
            print(' '.join(reversed_list_with_chars))


if __name__ == '__main__':
    user_rows, user_columns = get_user_input()
    show_chessboard(user_rows, user_columns)
