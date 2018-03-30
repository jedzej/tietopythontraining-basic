def knight_move():
    first_column = int(input())
    first_row = int(input())
    second_column = int(input())
    second_row = int(input())
    if (abs(first_column - second_column) == 1 and abs(first_row - second_row) == 2) or (abs(first_column - second_column) == 2 and abs(first_row - second_row) == 1):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    knight_move()