start_col = int(input('Enter column for STARTING position\n'))
start_row = int(input('Enter row STARTING position\n'))
end_col = int(input('Enter column for ENDING position\n'))
end_row = int(input('Enter row for ENDING position\n'))
distanc_col = abs(start_col - end_col)
distanc_row = abs(start_row - end_row)
if distanc_col == distanc_row:
    print('YES')
else:
    print('NO')
