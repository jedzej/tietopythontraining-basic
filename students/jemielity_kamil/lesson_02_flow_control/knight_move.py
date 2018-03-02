starting_column = int(input('Start column: '))
starting_row = int(input('Start row: '))

ending_column = int(input('Ending column: '))
ending_row = int(input('Ending row: '))

if abs(starting_column - ending_column) == 2:
    if ending_row == starting_row + 1 or starting_row - 1:
        print('YES')
    else:
        print('NO')
elif abs(starting_row - ending_row) == 2:
    if ending_column == starting_column + 1 or starting_column - 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
