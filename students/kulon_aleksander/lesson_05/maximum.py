m, n = [int(s) for s in input().split()]
max_i, max_j = m + 1, n + 1
tab = []

for i in range(m):
    tab.append(input().split())
    if i == 0:
        max = int(tab[0][0])
    for j in range(n):
        if int(tab[i][j]) > max:
            max = int(tab[i][j])
            max_i, max_j = i, j
        elif int(tab[i][j]) == max:
            if i < max_i:
                max_i, max_j = i, j
            elif i == max_i and j < max_j:
                max_i, max_j = i, j

print(max_i, max_j)
