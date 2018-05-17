# Program print/return changed array , as for x, y grid
# You can think of grid[x][y] as being the character at the
# x- and y-coordinates of a “picture” drawn with text characters.
# The (0, 0) origin will be in the upper-left corner,
# the x-coordinates increase going right,
# and the y-coordinates increase going down.

grid1 = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

grid2 = [['a', '1', 'c', '.', '.'],
         ['b', '2', 'O', '3', '.'],
         ['f', '3', 'w', '.', '.']]


def change_grid(grid):
    new_list = [[0] * len(grid) for i in range(len(grid[0]))]
    for i in range(len(grid[0])):
        k = len(grid) - 1
        for j in range(len(grid)):
            new_list[i][j] = grid[k][i]
            k -= 1
    # print list
    for row in new_list:
        print(' '.join([str(elem) for elem in row]))
    return new_list


change_grid(grid1)
print("")
change_grid(grid2)
