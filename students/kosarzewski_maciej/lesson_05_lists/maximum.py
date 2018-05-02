index = [0, 0]
m, n = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]

number = a[0][0]
for i in range(m):
    if max(a[i]) > number:
        number = max(a[i])
        index[0] = i
        index[1] = a[i].index(number)

print(index[0], index[1])
