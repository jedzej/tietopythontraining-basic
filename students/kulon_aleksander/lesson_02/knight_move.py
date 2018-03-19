cell1_x = int(input())
cell1_y = int(input())

cell2_x = int(input())
cell2_y = int(input())

if ((cell1_y + 2 == cell2_y) or (cell1_y - 2 == cell2_y)) and ((cell1_x + 1 == cell2_x) or (cell1_x - 1 == cell2_x)):
    print('YES')
elif ((cell1_x + 2 == cell2_x) or (cell1_x - 2 == cell2_x)) and ((cell1_y + 1 == cell2_y) or (cell1_y - 1 == cell2_y)):
    print('YES')
else:
    print('NO')
