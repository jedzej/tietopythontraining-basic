
starting_column = int(input('Start column: '))
starting_row = int(input('Start row: '))

ending_column = int(input('Ending column: '))
ending_row = int(input('Ending row: '))

if starting_column > ending_column:
    difference = starting_column - ending_column
else:
    difference = ending_column - starting_column

if starting_row - difference == ending_row or starting_row + difference == ending_row:
    print('YES')
elif starting_row == ending_row or starting_column == ending_column:
    print('YES')
else:
    print('NO')
