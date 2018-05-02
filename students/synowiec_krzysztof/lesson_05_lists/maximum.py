def main():
    rows, columns = [int(x) for x in input().split()]
    table = [[int(y) for y in input().split()] for x in range(rows)]
    max_row, max_column = 0, 0
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] > table[max_row][max_column]:
                max_row, max_column = x, y

    print("{} {}".format(max_row, max_column))


if __name__ == '__main__':
    main()
