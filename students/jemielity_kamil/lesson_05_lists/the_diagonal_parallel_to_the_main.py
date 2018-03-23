n = int(input('n: '))

array = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        array[i][j] = abs(i - j)

for i in range(len(array)):
    for j in range(len(array[i])):
        print(str(array[i][j]), end=' ')
    print()



