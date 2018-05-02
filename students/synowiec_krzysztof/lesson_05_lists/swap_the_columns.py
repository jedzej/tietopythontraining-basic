def main():
    rows, columns = [int(x) for x in input().split()]
    matrix = [[int(y) for y in input().split()] for x in range(rows)]
    i, j = [int(x) for x in input().split()]
    matrix = swap_columns(matrix, i, j)
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()


def swap_columns(matrix, i, j):
    tmp_column = [row[i] for row in matrix]
    for x in range(len(matrix)):
        matrix[x][i] = matrix[x][j]
        matrix[x][j] = tmp_column[x]
    return matrix


if __name__ == '__main__':
    main()
