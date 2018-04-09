a = [int(i) for i in input().split()]
min_idx = 0
max_idx = 0

for i in range(1, len(a)):
    if a[i] < a[min_idx]:
        min_idx = i
    elif a[i] > a[max_idx]:
        max_idx = i

a[min_idx], a[max_idx] = a[max_idx], a[min_idx]
print(' '.join([str(i) for i in a]))
