n = int(input())

sum = 0
for i in range(1, n + 1):
    sum += i

for i in range(1, n):
    sum -= int(input())

print(sum)
