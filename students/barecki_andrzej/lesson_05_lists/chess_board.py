row_number, column_number = [int(x) for x in input().split()]
matrix = [["."] * column_number for i in range(row_number)]
for row in range(row_number):
    for column in range(column_number):
        if (row % 2 == 1 and column % 2 == 0) or\
                (row % 2 == 0 and column % 2 == 1):
            matrix[row][column] = "*"
for row in matrix:
    print(' '.join([str(elem) for elem in row]))
