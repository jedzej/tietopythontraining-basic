result = 0
tmp = 1
value = int(input())
for i in range(1, value+1):
    tmp = tmp * i
    result += tmp
print(result)
