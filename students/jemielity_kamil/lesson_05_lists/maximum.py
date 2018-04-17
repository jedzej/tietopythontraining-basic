rows_and_columns = [int(i) for i in input('Numbers: ').split()]
m = rows_and_columns[0]  # rows
n = rows_and_columns[1]  # columns

array = [[int(j) for j in input('Numbers in row: ').split()] for k in range(m)]

maximum_i = 0
maximum_j = 0
maximum = array[maximum_i][maximum_j]

for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j] > maximum:
            maximum, maximum_i, maximum_j = array[i][j], i, j
print(str(maximum_i) + " " + str(maximum_j))
