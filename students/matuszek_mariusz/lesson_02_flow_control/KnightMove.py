FirstColumn = int(input('First column: '))
FirstRow = int(input('First row: '))
SecondColumn = int(input('Second column: '))
SecondRow = int(input('Second row: '))

Pos1 = abs(FirstColumn - SecondColumn)
Pos2 = abs(FirstRow - SecondRow)

if (Pos1 == 2 and Pos2 == 1) or (Pos2 == 2 and Pos1 == 1):
    print('YES')
else:
    print('NO')
