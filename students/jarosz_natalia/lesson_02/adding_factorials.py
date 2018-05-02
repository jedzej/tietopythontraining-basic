n = int(input())
y = 1
result = 0

for i in range(1, n + 1):
    y *= i
    result += y
print(result)
