n, m = input().split()
tab = []
for i in range(int(n)):
    tab.append(['*'] * int(m))
    for j in range(int(m)):
        if i % 2 == 0 and j % 2 == 0:
            tab[i][j] = '.'
        elif i % 2 and j % 2:
            tab[i][j] = '.'
    print(' '.join(tab[i]))
