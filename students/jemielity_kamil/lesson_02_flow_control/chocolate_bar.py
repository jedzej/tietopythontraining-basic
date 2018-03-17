
n = int(input("Length of chocolate: "))
m = int(input("Width of chocolate "))
k = int(input("Number of squares: "))

flag = 0

if m*n % k == 0 and k != 1:
    flag = 1

for row in range(n, 1, -1):
    if row * m == k:
        flag = 1
        break

for column in range(m, 1, -1):
    if column * n == k:
        flag = 1
        break

if flag == 1:
    print('YES\n')
else:
    print('NO\n')
