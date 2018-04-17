def data_input():
    data_in = input().split(" ")
    result = []
    for i in data_in:
        result.append(int(i))
    return result


def insert_matrix(m):
    matrix = []
    for i in range(m):
        matrix.append(data_input())
    return matrix


def swap_columns(a, i, j):
    for n in a:
        n_new = n[i]
        n[i] = n[j]
        n[j] = n_new
    return a


numbers = data_input()
number_rows = numbers[0]
number_columns = numbers[1]
new_matrix = insert_matrix(number_rows)
numbers = data_input()
column_i = numbers[0]
column_j = numbers[1]
array = swap_columns(new_matrix, column_i, column_j)

for i in range(number_rows):
    print(''.join(str(array[i])))
