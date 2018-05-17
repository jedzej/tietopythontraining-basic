x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

# there are 8 possible moves from point 1

pos_moves = [x_1 + 1, y_1 + 2], [x_1 + 1, y_1 - 2], [x_1 - 1, y_1 + 2],\
            [x_1 - 1, y_1 - 2], [x_1 + 2, y_1 + 1], \
            [x_1 + 2, y_1 - 1], [x_1 - 2, y_1 + 1], [x_1 - 2, y_1 - 1]

res = False
for point in pos_moves:
    if point[0] == x_2 and point[1] == y_2:
        res = True

if res:
    print('YES')
else:
    print('NO')
