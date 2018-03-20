
start_column = int(input('Start column: '))
start_row = int(input('Start row: '))

end_column = int(input('Ending column: '))
end_row = int(input('Ending row: '))

if abs(start_column - end_column) == 2:

    if end_row == start_row + 1 or end_row == start_row - 1:
        print('YES')
    else:
        print('NO')
elif abs(start_row - end_row) == 2:
    if end_column == start_column + 1 or end_column == start_column - 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
