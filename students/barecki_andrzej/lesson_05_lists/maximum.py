row_number, column_number = [int(x) for x in input().split()]
input_data = []
# Set input data
for row in range(row_number):
    input_data.append([int(j) for j in input().split()])
index_x = 0
index_y = 0
max_value = input_data[0][0]
# Search maximum value in matrix
for row in range(row_number):
    for column in range(column_number):
        if input_data[row][column] > max_value:
            max_value = input_data[row][column]
            index_x = row
            index_y = column
print(str(index_x) + " " + str(index_y))
