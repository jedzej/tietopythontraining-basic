base_x = int(input())
base_y = int(input())
direct_x = int(input())
direct_y = int(input())
if (abs(direct_x - base_x) == 2) and (abs(direct_y - base_y) == 1):
    print('YES')
elif (abs(direct_x - base_x) == 1) and (abs(direct_y - base_y) == 2):
    print('YES')
else:
    print('NO')
