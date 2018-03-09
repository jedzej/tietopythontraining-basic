x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 2 and dy == 1 or dy == 2 and dx == 1:
    print('YES')
else:
    print('NO')
