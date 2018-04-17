def count_maximum(rows, columns, a):
    maximum = a[0][0]
    max_row, max_col = 0, 0

    for i in range(rows):
        for j in range(columns):
            if a[i][j] > maximum:
                maximum = a[i][j]
                max_row, max_col = i, j

    print(max_row, max_col)


def main():
    rows, col = [int(i) for i in input("Input rows and columns: ").split()]
    a = [[int(j) for j in input("Input " + str(col) + " values: ").split()]
         for i in range(rows)]

    count_maximum(rows, col, a)


if __name__ == '__main__':
    main()
