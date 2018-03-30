base_x = int(input())
base_y = int(input())
direct_x = int(input())
direct_y = int(input())
if abs(direct_x - base_x) == abs(direct_y - base_y):
    print('YES')
else:
    print('NO')
