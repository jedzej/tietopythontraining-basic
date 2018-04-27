size = int(input('Give the size: '))

matrix = []
for i in range(size):
    array = []
    for j in range(size):
        if j >= i:
            array.append(j-i)
        if j < i:
            array.append(i-j)
    matrix.append(array)

print('Result: ')
for i in range(size):
    print(matrix[i])
