number = int(input('Give the number: '))

for j in range(1, number+1):
    for i in range(1, j+1):
        print(i, sep='', end='')
    print()