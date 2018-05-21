
def maximum():

    rows, columns = [int(i) for i in input().split()]
    array = [[int(j) for j in input().split()] for i in range(rows)]

    max_i, max_j = 0, 0
    max_index_value = array[0][0]

    for i in range(rows):
        for j in range(columns):
            if array[i][j] > max_index_value:
                max_index_value = array[i][j]
                max_i, max_j = i, j

    print(max_i, max_j)


if __name__ == '__main__':
    maximum()
