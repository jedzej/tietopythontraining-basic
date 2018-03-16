def check_if_queen_will_move():
    initial_column = int(input())
    initial_row = int(input())
    final_column = int(input())
    final_row = int(input())
    if abs(initial_column - final_column) == abs(initial_row - final_row) or \
            initial_column == final_column or initial_row == final_row:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    check_if_queen_will_move()
