a = [int(s) for s in input().split()]
quantity = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        quantity += 1
print(quantity)
