# piotrsta
# Chess board
# https://snakify.org/lessons/two_dimensional_lists_arrays/problems/chessboard/# piotros0

n, m = 3, 4

for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 == 0 :
            print('.', end=' ')
        elif i % 2 == 1 and j % 2 == 1 :
            print('.', end=' ')
        else:
            print('*', end=' ')
        if j == (m - 1):
            print('')
