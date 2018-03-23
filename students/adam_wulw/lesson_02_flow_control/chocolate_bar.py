n = int(input('Enter n\n'))
m = int(input('Enter m\n'))
k = int(input('Enter k\n'))
mn_min = min(n, m)
mn_max = max(n, m)
if (n * m > k):
    if ((k % n == 0) or (k % m == 0)):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
