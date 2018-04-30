a = input().split()
b = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] and a[i + 1] < a[i]:
        b += 1
print(b)
