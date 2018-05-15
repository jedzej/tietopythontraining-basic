n = int(input())

for l in range(1, n + 1):
    for x in range(1, l + 1):
        print(x, sep='', end='')
    print(end='\n')
