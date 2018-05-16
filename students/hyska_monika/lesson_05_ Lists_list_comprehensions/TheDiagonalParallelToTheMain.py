# Program print the diagonal parallel array


array_size = int((input("Size of array: ")))
diagonal_list = [[0] * array_size for i in range(array_size)]
for i in range(array_size):
    for j in range(array_size):
        if i == j:
            diagonal_list[i][j] = 0
        elif j > i:
            diagonal_list[i][j] = diagonal_list[i][j - 1] + 1
        else:
            diagonal_list[i][j] = diagonal_list[i - 1][j] + 1

# print list
for row in diagonal_list:
    print(' '.join([str(elem) for elem in row]))
