n = int(input('Enter a number: '))
listing = [[abs(i - j) for j in range(n)] for i in range(n)]

for i in listing:
    print(' '.join([str(x) for x in i]))
