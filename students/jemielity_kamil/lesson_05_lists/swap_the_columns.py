def swap_columns(a, i, j):

    for loop in range(len(a)):
        a[loop][i], a[loop][j] = a[loop][j], a[loop][i]

    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = str(a[i][j])

    return a


m, n = [int(i) for i in input('Number of lines and elements: ').split()]
array = []
for x in range(m):
    elements = [int(i) for i in input('Elements: ').split()]
    array.append(elements)

column1, column2 = [int(i) for i in input('Columns to swap: ').split()]
result = swap_columns(array, column1, column2)

for i in range(len(result)):
    new_array = ' '.join(result[i])
    print(new_array)
