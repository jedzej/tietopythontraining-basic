x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print('YES') if (x1-x2 == 0 or y1-y2 == 0 or abs(x1-x2) == abs(y1-y2)) else print('NO')

