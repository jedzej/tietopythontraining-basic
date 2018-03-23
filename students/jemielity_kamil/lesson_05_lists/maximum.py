rows_and_columns = [int(i) for i in input('Numbers: ').split()]
m = rows_and_columns[0]  # rows
n = rows_and_columns[1]  # columns

array = [[int(j) for j in input('Numbers in row: ').split()] for k in range(m)]

maximum = array[0][0]

for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j] > maximum:
            maximum = array[i][j]

for i in range(len(array)):
    try:
        print(str(i) + ' ' + str(array[i].index(maximum)))
        break
    except ValueError:
        continue







