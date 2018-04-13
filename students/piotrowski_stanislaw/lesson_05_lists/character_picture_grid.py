# piotrsta
# character picture grid
# https://automatetheboringstuff.com/chapter4/

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

output_string = ''
for i in range(len(grid[0])):
    for j in range(len(grid)):
        output_string += str(grid[j][i])
    print(output_string)
    output_string = ''
