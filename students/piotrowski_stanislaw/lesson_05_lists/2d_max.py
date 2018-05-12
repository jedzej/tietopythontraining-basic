# piotrsta
# Maximum
# https://snakify.org/lessons/two_dimensional_lists_arrays/problems/2d_max/

n, m = 3, 4
spam = [[0, 3, 2, 4], [2, 3, 5, 5], [5, 1, 2, 3]]

row_max = 0
col_max = 0
value_max = spam[row_max][col_max]

for i in range(n):
    for j in range(m):
        if spam[i][j] > value_max:
            value_max = spam[i][j]
            row_max = i
            col_max = j
print(row_max, col_max)
