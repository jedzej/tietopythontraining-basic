def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]


m, n = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
i, j = [int(i) for i in input().split()]

swap_columns(a, i, j)

for i in a:
    print(" ".join([str(element) for element in i]))
