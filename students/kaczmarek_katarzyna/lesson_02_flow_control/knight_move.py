col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())
deltaCol = abs(col1 - col2)
deltaRow = abs(row1 - row2)
if deltaCol == 1 and deltaRow == 2 or deltaCol == 2 and deltaRow == 1:
    print('YES')
else:
    print('NO')
