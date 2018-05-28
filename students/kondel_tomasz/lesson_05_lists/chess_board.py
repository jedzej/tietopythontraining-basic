n, m = list(int(x) for x in input().split())

for y in range(n):
    row = []
    isDot = y % 2 == 0
    for x in range(m):
        row.append("." if isDot else "*")
        isDot = not isDot
    print(''.join(row))
