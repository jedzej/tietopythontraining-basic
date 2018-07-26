m, n = (int(i) for i in input().split())
chessboard = []

for x in range(m):
    chessboard.append([])
    for y in range(n):
        if (x + y) % 2 != 0:
            chessboard[x].append('*')
        else:
            chessboard[x].append('.')

for row in chessboard:
    print(' '.join(row))