def swap_columns(a, i, j):
    for n in range(len(a)):
        a[n][i], a[n][j] = a[n][j], a[n][i]


def main():
    rows, col = [int(i) for i in input("Input rows and columns: ").split()]
    a = [[int(j) for j in input(str(col) + " values:").split()] for i in range(rows)]
    swap_col, swap_col2 = [int(i) for i in input("Columns to swap: ").split()]

    swap_columns(a, swap_col, swap_col2)
    print('\n'.join([' '.join([str(i) for i in row]) for row in a]))


if __name__ == '__main__':
    main()
