#Given an integer n, produce a two-dimensional array of size (n x n) and complete it according to the following rules, and print with a single space between characters:
#On the main diagonal write 0 .
#On the diagonals adjacent to the main, write 1 .
#On the next adjacent diagonals write 2 and so forth.
#Print the elements of the resulting array.

print("Enter the square matrix size:")
n = int(input())

matrix = []
row = []
for i in range(n):
    for j in range(0-i, n-i):
        row.append(abs(j))
    
    matrix.append(row)
    row = []

#print the matrix
for i in range(n):
    for j in range(n):
        if j == n-1:
            print(matrix[i][j])
        else:
            print(matrix[i][j], end=" ")

