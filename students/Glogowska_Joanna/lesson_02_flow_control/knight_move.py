print('Enter coordinates (numbers 1-8)')
print('Starting column: ')
scolumn = int(input())
print('Starting row: ')
srow = int(input())
print('Ending column: ')
ecolumn = int(input())
print('Ending square row: ')
erow = int(input())
print('Can knight go from starting position \
to ending position in one move?')
columns = abs(scolumn - ecolumn)
rows = abs(srow - erow)
if (columns == 1 and rows == 2) or (columns == 2 and rows == 1):
    print('YES')
else:
    print('NO')
