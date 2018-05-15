n, m = [int(i) for i in input().split()]
a = []

for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')

for row in a:
    print(' '.join(row))
