n = int(input())
m = int(input())
k = int(input())

print ('YES')  if (k % m == 0 or k % n == 0) and k < m*n  else print('NO')

