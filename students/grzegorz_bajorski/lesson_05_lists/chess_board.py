n, m = [int(i) for i in input().split()]
tab = []

for i in range(n):
    tab.append([])
    for j in range(m):
        if (i + j) % 2:
            tab[i].append('*')
        else:
            tab[i].append('.')

for row in tab:
    print(' '.join(row))
