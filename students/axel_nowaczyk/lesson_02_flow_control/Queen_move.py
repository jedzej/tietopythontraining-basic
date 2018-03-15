def queen_move():
    first_column = int(input())
    first_row = int(input())
    second_column = int(input())
    second_row = int(input())
    if first_column == second_column or first_row == second_row or abs(first_column - second_row) == abs(first_row - second_column) or abs(first_column - second_column) == abs(first_row - second_row):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    queen_move()