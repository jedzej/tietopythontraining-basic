
start_column = int(input('Start column: '))
start_row = int(input('Start row: '))

end_column = int(input('Ending column: '))
end_row = int(input('Ending row: '))

if start_column > end_column:
    diff = start_column - end_column
else:
    diff = end_column - start_column

if start_row - diff == end_row or start_row + diff == end_row:
    print('YES')
elif start_row == end_row or start_column == end_column:
    print('YES')
else:
    print('NO')
