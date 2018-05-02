n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
            a[i].append(abs(i - j))

for row in a:
    print(' '.join(str(i) for i in row))
