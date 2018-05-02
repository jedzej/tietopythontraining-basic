def swap_columns(a, i, j):
    for row in range(len(a)):
        anteroom = a[row][i]
        a[row][i] = a[row][j]
        a[row][j] = anteroom
    return a


m, n = [int(s) for s in input().split()]
A = [[int(s) for s in input().split()] for s in range(m)]
first_column, second_column = [int(s) for s in input().split()]
if (first_column < n) and (second_column < n):
    result = swap_columns(A, first_column, second_column)
    for row11 in result:
        print(' '.join([str(elem) for elem in row11]))
