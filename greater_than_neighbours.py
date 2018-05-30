n = [int(i) for i in input().split()]
quantity = 0

for i in range(1, len(n) - 1):
    if (n[i] > n[i - 1]) and (n[i] > n[i + 1]):
        quantity += 1

print(quantity)