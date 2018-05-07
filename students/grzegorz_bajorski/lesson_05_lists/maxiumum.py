m, n = [int(i) for i in input().split()]
table = []
row_max = col_max = 0

for _ in range(m):
        table.append([int(i) for i in input().split()])

for i in range(m):
    for j in range(n):
        if table[i][j] > table[row_max][col_max]:
                row_max = i
                col_max = j

print(str(row_max) + ' ' + str(col_max))
