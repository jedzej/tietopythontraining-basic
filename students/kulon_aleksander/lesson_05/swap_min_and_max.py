a = [int(i) for i in input().split()]
max = 0
min = 0

for i in range(len(a)):
    if a[i] > max:
        max = a[i]

min = max

for i in range(len(a)):
    if a[i] < min:
        min = a[i]

index_min = a.index(min)
index_max = a.index(max)

a[index_min] = max
a[index_max] = min

print(''.join(a))
