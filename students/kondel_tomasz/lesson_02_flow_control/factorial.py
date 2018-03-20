n = int(input())
res = 1
for x in range(1, n + 1):
    res = res * x
if n >= 0:
    print(res)
else:
    print('0')
