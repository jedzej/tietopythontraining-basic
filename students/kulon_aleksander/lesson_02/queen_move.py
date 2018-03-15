cell1_x = int(input())
cell1_y = int(input())

cell2_x = int(input())
cell2_y = int(input())

distance_x = abs(cell1_x - cell2_x)
distance_y = abs(cell1_y - cell2_y)

if ((cell1_x - distance_x == cell2_x) or (cell1_x + distance_x == cell2_x)) \
   and ((cell1_y - distance_x == cell2_y) \
        or (cell1_y + distance_x == cell2_y)):
    print('YES')
elif distance_y == 0:
    print('YES')
elif distance_x == 0:
    print('YES')
else:
    print('NO')
