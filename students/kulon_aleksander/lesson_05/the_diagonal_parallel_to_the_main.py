n = int(input())
a = []

for y in range(n):
    a.append([0] * n)
    for x in range(n):
        if y == 0:
            a[y][x] = x
        else:
            a[y][x] = abs(x - y)

print('\n'.join([' '.join([str(i) for i in row]) for row in a]))
