def swap_function(matrix, first, second):
    for r in range(0, len(matrix)):
        matrix[r][first], matrix[r][second] = \
            matrix[r][second], matrix[r][first]


row_number, column_number = [int(x) for x in input().split()]
input_data = []
# Set input data
for row in range(row_number):
    input_data.append([int(j) for j in input().split()])

"""Select columns for swap"""
swap_a, swap_b = [int(x) for x in input().split()]

swap_function(input_data, swap_a, swap_b)
"""Print result"""
for row in input_data:
    print(' '.join([str(elem) for elem in row]))
