def main():
    rows, columns = [int(x) for x in input().split()]
    board = [[dot_or_ast(x, y) for y in range(columns)] for x in range(rows)]

    for row in board:
        for column in row:
            print(column, end=" ")
        print()


def dot_or_ast(x, y):
    if (y + x) % 2:
        return "*"
    else:
        return "."


if __name__ == '__main__':
    main()
