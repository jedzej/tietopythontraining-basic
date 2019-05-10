row, column = [int(i) for i in input("Give me two numbers n and m"
                              "\n so I can populate it: ").split()]

matrix = []

for i in range(row):
    matrix.append([])
    for j in range(column):
        if (i + j) % 2 == 0:
            matrix[i].append('.')
        else:
            matrix[i].append('*')
            
for row in matrix :
    print(' '.join(row))