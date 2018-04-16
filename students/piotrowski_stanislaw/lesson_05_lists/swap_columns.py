# piotrsta
# Swap the columns
# https://snakify.org/lessons/two_dimensional_lists_arrays/problems/swap_columns/


def swap_columns(table, x, y):
    for row in range(len(table)):
        table[row][x], table[row][y] = table[row][y], table[row][x]
    return table


if __name__ == '__main__':
    n, m = 3, 4
    spam = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
    i, j = 0, 1

    swap_columns(spam, i, j)

    for i in spam:
        print(' '.join([str(j) for j in i]))
