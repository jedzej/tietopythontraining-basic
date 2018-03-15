n = int(input())
result = 0

for i in range(1, n + 1):
    result += i

for i in range(1, n):
    result -= int(input())
print(result)
