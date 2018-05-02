print('Enter coordinates (numbers 1-8)')
print('Starting column: ')
scolumn = int(input())
print('Starting row: ')
srow = int(input())
print('Ending column: ')
ecolumn = int(input())
print('Ending square row: ')
erow = int(input())
print('Can bishop go from starting position \
to ending position in one move?')
if abs(scolumn - ecolumn) == abs(srow - erow):
    print("YES")
else:
    print("NO")
