n, m = [int(i) for i in input('Numbers: ').split()]

array = [[0 for j in range(m)] for i in range(n)]

for j in range(m):
    for i in range(n):
        if (i + j) % 2 is 0:
            array[i][j] = '.'
        else:
            array[i][j] = '*'

for i in range(len(array)):
    new_array = ' '.join(array[i])
    print(new_array, end='')
    print()
