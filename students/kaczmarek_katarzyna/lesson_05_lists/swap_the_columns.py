def swap_columns(a, i, j):
    for n in range(len(a)):
        a[n][i], a[n][j] = a[n][j], a[n][i]


def main():
    rows, columns = [int(i) for i
                     in input("Number of rows and columns "
                              "(space separated): ").split()]
    array = [[int(j) for j
              in input("[Row " + str(row + 1) + "] "
                       "Input " + str(columns) + " values "
                       "(space separated): ").split()]
             for row in range(rows)]
    swap_col_1, swap_col_2 = [int(i) for i
                              in input("Columns to swap "
                                       "(space separated): ").split()]

    swap_columns(array, swap_col_1, swap_col_2)
    print('\n'.join([' '.join([str(i) for i in row]) for row in array]))


if __name__ == '__main__':
    main()
