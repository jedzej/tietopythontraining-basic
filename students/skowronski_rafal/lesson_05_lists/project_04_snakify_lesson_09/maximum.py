def get_maximum_index(matrix):
    maximum_index = (0, 0)
    maximum = matrix[maximum_index[0]][maximum_index[1]]

    rows_count = len(matrix)
    cols_count = len(matrix[0])
    for row_index in range(rows_count):
        for col_index in range(cols_count):
            if maximum < matrix[row_index][col_index]:
                maximum_index = (row_index, col_index)
                maximum = matrix[row_index][col_index]

    return maximum_index


if __name__ == '__main__':
    rows_number = int(input('Enter number of rows: '))
    cols_number = int(input('Enter number of columns: '))

    print('Enter content of the matrix. Elements separated with \'space\'' +
          'and rows with ENTER: ')
    matrix = [[int(j) for j in input().split()[:cols_number]]
              for i in range(rows_number)]

    maximum_index = get_maximum_index(matrix)

    print('Index of maximum item: {0}, {1}'
          .format(maximum_index[0], maximum_index[1]))
