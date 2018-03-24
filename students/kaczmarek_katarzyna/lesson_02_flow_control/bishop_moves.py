col1 = int(input("From column: "))
row1 = int(input("From row: "))
col2 = int(input("To column: "))
row2 = int(input("To row: "))
if abs(col1 - col2) == abs(row1 - row2):
    print('YES')
else:
    print('NO')
