def find_max(rows, columns, array):
    maximum = array[0][0]
    max_row, max_col = 0, 0

    for i in range(rows):
        for j in range(columns):
            if array[i][j] > maximum:
                maximum = array[i][j]
                max_row, max_col = i, j

    print(max_row, max_col)


def main():
    rows, columns = [int(i) for i
                     in input("Number of rows and columns "
                              "(space separated): ").split()]
    array = [[int(j) for j
              in input("[Row " + str(row + 1) + "] "
                       "Input " + str(columns) + " values "
                       "(space separated): ").split()]
             for row in range(rows)]

    find_max(rows, columns, array)


if __name__ == '__main__':
    main()
