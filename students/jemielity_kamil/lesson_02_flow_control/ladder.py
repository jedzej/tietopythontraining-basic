
number = int(input('Integer: '))

for row in range(1, number+1):
    for i in range(1, row+1):
        print(i, end='')

    print(sep='')
