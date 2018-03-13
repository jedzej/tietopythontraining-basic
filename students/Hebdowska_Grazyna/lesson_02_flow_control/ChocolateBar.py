import math
n = int(input('n: '))
m = int(input('m: '))
k = int(input('k: '))

if (n * m > k):
    if (k >= n or k >= m):
        if k % n == 0:
            print('yes')
        elif k % m == 0:
	        print('yes')
        else:
	        print('no')

else:
    print('no')
