firstColumn = int(input("Enter first column: "))
firstRow = int(input("Enter first row: "))
secondColumn = int(input("Enter second column: "))
secondRow = int(input("Enter second row: "))

row = abs(firstRow-secondRow)
column = abs(firstColumn-secondColumn)

if row == column or firstRow == secondRow or firstColumn == secondColumn:
    print("YES - we can move the queen there!")
else:
    print("NO - we can't move queen there")
