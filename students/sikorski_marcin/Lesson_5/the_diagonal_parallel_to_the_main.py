size_of_matrix = int(input("Give me an integer to produce the matrix: "))

matrix = [[abs(i - j) for j in range(size_of_matrix)] for i in range(size_of_matrix)]
for row in matrix:
    print(' '.join([str(i) for i in row]))