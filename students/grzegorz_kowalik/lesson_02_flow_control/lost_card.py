n = int(input())

total = (1 + n) / 2 * n

for i in range(1, n):
    total -= int(input())

print(int(total))
