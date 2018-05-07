n = int(input())
result = 0

for i in range(1, n + 1):
    if int(input()) == 0:
        result = result + 1
print(result)
