n, k = [int(s) for s in input().split()]
pins = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        pins[j] = '.'
print(''.join(pins))
