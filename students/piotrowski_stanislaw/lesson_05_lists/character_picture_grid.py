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

<<<<<<< HEAD:students/piotrowski_stanislaw/lesson_05_lists/character_picture_grid.py
output_string = ''
for i in range(len(grid[0])):
    for j in range(len(grid)):
        output_string += str(grid[j][i])
    print(output_string)
    output_string = ''
=======

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end="")
    print('')

# shorter (though more advanced) options is:

# print('\n'.join(map(''.join, zip(*grid))))
>>>>>>> bb5a63aac91aa9862cfb521af4327c64e9b1e919:students/arkadiusz_kasprzyk/lesson_05_lists/charachter_picture_grid.py
