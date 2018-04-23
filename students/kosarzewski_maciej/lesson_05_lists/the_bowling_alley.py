n, k = [int(s) for s in input().split()]
alley = ['I'] * n
list_alley = list(alley)
if k > 0:
    for i in range(k):
        a = [int(s) for s in input().split()]
        for j in range(a[0] - 1, a[1]):
            list_alley[j] = "."
print(''.join(list_alley))
