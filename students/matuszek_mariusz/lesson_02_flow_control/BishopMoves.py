FirstColumn = int(input('First column: '))
FirstRow = int(input('First row: '))
SecondColumn = int(input('Second column: '))
SecondRow = int(input('Second row: '))

Pos1 = abs(FirstColumn - SecondColumn)
Pos2 = abs(FirstRow - SecondRow)

if Pos1 == Pos2:
    print('YES')
else:
    print('NO')
