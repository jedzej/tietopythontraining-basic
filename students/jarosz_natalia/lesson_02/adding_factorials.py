n = int(input())
result = 0
y = 1

for i in range(1, n + 1):
    for x in range(1, i + 1):
        y *= x
    result += y
print(result)
