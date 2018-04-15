def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]

m, n = [int(i) for i in input().split()]
a = []

for i in range(m):
    a.append([int(j) for j in input().split()])

i, j = [int(i) for i in input().split()]

swap_columns(a, i, j)

for i in a:
    print(' '.join([str(elem) for elem in i]))
