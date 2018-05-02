size = int(input())
matrix = [[0] * size for i in range(size)]
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if column < row:
            matrix[row][column] = matrix[column][row]
        else:
            matrix[row][column] = ((column - row) % size)
"""Print result"""
for row in matrix:
    print(' '.join([str(elem) for elem in row]))
