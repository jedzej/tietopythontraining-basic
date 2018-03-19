
start_column = int(input('Start column: '))
start_row = int(input('Start row: '))

end_column = int(input('Ending column: '))
ending_row = int(input('Ending row: '))

if start_column > end_column:
    diff = start_column - end_column
else:
    diff = end_column - start_column

if start_row - diff == ending_row or start_row + diff == ending_row:
    print('YES')
else:
    print('NO')
