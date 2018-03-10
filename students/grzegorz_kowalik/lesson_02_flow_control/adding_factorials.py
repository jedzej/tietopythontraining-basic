n = int(input())

tmp_factorial = 1
res = 0
for i in range(1, n+1):
    tmp_factorial *= i
    res += tmp_factorial

print(res)
