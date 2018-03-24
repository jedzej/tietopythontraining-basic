start_col = int(input('Enter column for STARTING position\n'))
start_row = int(input('Enter row STARTING position\n'))
end_col = int(input('Enter column for ENDING position\n'))
end_row = int(input('Enter row for ENDING position\n'))
distanc_col = abs(start_col - end_col)
distanc_row = abs(start_row - end_row)
if distanc_col < 1 or distanc_row < 1:
    print('NO')
elif (distanc_col + distanc_row) != 3:
    print('NO')
elif distanc_col == distanc_row/2 or distanc_col/2 == distanc_row:
    print('YES')
else:
    print('NO')
