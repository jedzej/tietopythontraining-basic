from helper import print_matrix_as_string


def swap_columns(a, i, j):
    for row in range(len(a)):
        tmp = a[row][i]
        a[row][i] = a[row][j]
        a[row][j] = tmp


if __name__ == '__main__':
    rows_number = int(input('Enter number of rows: '))
    cols_number = int(input('Enter number of columns: '))

    print('Enter content of the matrix. Elements separated with \'space\'' +
          'and rows with ENTER: ')
    matrix = [[int(j) for j in input().split()[:cols_number]]
              for i in range(rows_number)]

    first_column = int(input('Enter first column number to swap: '))
    second_column = int(input('Enter second column number to swap: '))

    swap_columns(matrix, first_column, second_column)
    print_matrix_as_string(matrix)
