n = int(input())
m = int(input())
k = int(input())

if (k <= m * n) and ((m * n - k) % m == 0 or (m * n - k) % n == 0):
    print('YES')
else:
    print('NO')
