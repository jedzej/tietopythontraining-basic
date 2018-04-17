# The program reads three integers: n, m, and k. It should print YES if split chocolate bar will have k squares or//
# NO if not.


print('n x m portions: ')
n = int(input())
print(' x ')
m = int(input())

print('k squares: ')
k = int(input())

bar = n * m
print('Number of whole squares in chocolate bar: ' + str(bar))
if bar >= k:
    if k / n == int(k / n):
        print('YES')
    elif k / m == int(k / m):
        print('YES')
    else:
        print('NO')
else:
    print('NO')