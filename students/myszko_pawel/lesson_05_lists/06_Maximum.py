# Given two integers representing the rows and columns (m×n),
# and subsequent m rows of n # elements, find the index position
# of the maximum element and print two numbers representing the index (i×j)
# or the row number and the column number. If there exist multiple
# such elements in different rows, print the one with smaller row number.
# If there multiple such elements occur on the same row, output the smallest column number.


def main():
    rows, columns = [int(s) for s in input().split()]
    matrix = []
    max_val_row = 0
    max_val_column = 0

    for i in range(0, rows):
#        matrix.append([])
#        for j in range(0, 1):
#            matrix[i].input().split()
        matrix.append([int(j) for j in input().split()])

    print(matrix)


    for m in range(0, rows):
        for n in range(0, columns):
            print(matrix[m][n])
            if matrix[m][n] > matrix[max_val_row][max_val_column]:
#            if (int(matrix[m][n]) > max_val):#not working! why?
                max_val_row = m
                max_val_column = n

    print(max_val_row, max_val_column)

if __name__ == "__main__":
    main()
