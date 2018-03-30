def check_if_knight_will_move():
    initial_column = int(input())
    initial_row = int(input())
    final_column = int(input())
    final_row = int(input())

    if abs(initial_column - final_column) == 1 \
            and abs(initial_row - final_row) == 2 \
            or abs(initial_column - final_column) == 2 \
            and abs(initial_row - final_row) == 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    check_if_knight_will_move()
