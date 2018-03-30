# Read an integer:
# a = int(input())
# Print a value:
# print(a)

n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 and k / n < m) or (k % m == 0 and k / m < n):
    print('YES')
else:
    print('NO')
	
