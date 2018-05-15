N = int(input())

res = 0
fact = 1
for x in range(1, N + 1):
    fact = fact * x
    res = res + fact

print(res)
