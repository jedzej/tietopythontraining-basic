#Description too long to be put here. See for yourself at
#https://automatetheboringstuff.com/chapter4/
#"Character Picture Grid"

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

horizontal_len = len(grid[0])
vertical_len = len(grid)

for i in range(horizontal_len):
   for j in range(vertical_len):
       print(grid[j][i], end='')    
   print("")
