rows, columns = (int(i) for i in input().split())
matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

max = matrix[0][0]
max_row = 0
max_column = 0

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] > max:
            max = matrix[i][j]
            max_row = i
            max_column = j

print('Row: ' + str(max_row))
print('Column: ' + str(max_column))
