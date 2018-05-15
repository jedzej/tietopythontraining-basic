m, n = [int(i) for i in input().split()]
x = [[int(j) for j in input().split()] for i in range(m)]
row, col = 0, 0
current_max = x[0][0]

for i in range(m):
    for j in range(n):
        if x[i][j] > current_max:
            current_max = x[i][j]
            row, col = i, j

print(row, col)
