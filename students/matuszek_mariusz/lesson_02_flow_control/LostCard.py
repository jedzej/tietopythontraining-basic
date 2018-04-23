n = int(input('N = '))

lists = ''
c = 0

for i in range(1, n):
    k = int(input(str(i) + ' = '))
    lists += str(k)

for j in range(1, n):
    if lists.count(str(j)) == 0:
        print(j)
        c = 1

if c != 1:
    print(n-1)
