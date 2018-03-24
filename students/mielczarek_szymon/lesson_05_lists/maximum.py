m, n = [int(i) for i in input().split()]
a = []
max_row = 0
max_col = 0
for i in range(m):
    a.append([int(j) for j in input().split()])
    for k in range(n):
        if a[i][k] > a[max_row][max_col]:
            max_row, max_col = i, k
print(max_row, max_col)
