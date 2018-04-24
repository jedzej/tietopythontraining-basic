a = [int(i) for i in input().split()]
max_v = 0
min_v = 0

for i in range(len(a)):
    if a[i] > max_v:
        max_v = a[i]

min_v = max_v

for i in range(len(a)):
    if a[i] < min_v:
        min_v = a[i]

index_min = a.index(min_v)
index_max = a.index(max_v)

a[index_min] = max_v
a[index_max] = min_v

print(''.join(str(a)))
