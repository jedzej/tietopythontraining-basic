n = int(input())
tab = [[0] * n for i in range(n)]

count = 0
for i in range(n):
    count = i
    for j in range(n):

        if i < j:
            count = count + 1
            tab[i][j] = count
        if i > j:
            tab[i][j] = count
            count = count - 1
        print(tab[i][j], end=' ')
    print()
