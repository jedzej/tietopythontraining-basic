n = int(input())
m = int(input())
k = int(input())

total_portions = n * m

if k <= n * m:
    if k % n == 0 or k % m == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
