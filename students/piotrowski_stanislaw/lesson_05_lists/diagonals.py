# piotrsta
# The diagonal parallel to the main
# https://snakify.org/lessons/two_dimensional_lists_arrays/problems/diagonals/

n = int(input())
m = n
spam = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        spam[i][j] = abs(j - i)

for i in spam:
    print(' '.join([str(j) for j in i]))
