grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print('')


'''   
print(grid[0][0]+grid[1][0]+grid[2][0]+grid[3][0]+grid[4][0]+grid[5][0]+grid[6][0]+grid[7][0]+grid[8][0])
print(grid[0][1]+grid[1][1]+grid[2][1]+grid[3][1]+grid[4][1]+grid[5][1]+grid[6][1]+grid[7][1]+grid[8][1])
'''