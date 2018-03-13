N = int(input('N: '))
l = []

for i in range(0,N - 1):
   n = int(input('n: '))
   if (0 < n) and (n <= N):
       l.append(n)

for i in range(1,N + 1):
    if i not in l:
       print(i)
