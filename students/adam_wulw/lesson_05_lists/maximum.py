input_str = input()
m, n = map(int, input_str.split())
tab = [0] * m

for i in range(m):
    tab[i] = input().split()

last_max = 0
max_i = 1
max_j = 1

for i in range(m):
    for j in range(n):
        value = int(tab[i][j])
        if value > last_max:
            last_max = value
            max_j = j
            max_i = i

print(max_i, max_j)
