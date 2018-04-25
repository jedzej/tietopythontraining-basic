#Given two integers representing the rows and columns (m x n), and subsequent m rows of n elements, find the index position of the maximum element and print two numbers representing the index (i x j) or the row number and the column number. If there exist multiple such elements in different rows, print the one with smaller row number. If there multiple such elements occur on the same row, output the smallest column number.

print("Enter input list dimensions:")
m, n = [int(i) for i in input().split()]

input_list = []
for i in range(m):
    row = []
    while (len(row) != n):
        row = [int(i) for i in input().split()]
        if (len(row) != n):
            print("Wrong number of items (should be " + str(n) + ")")
        else:
            input_list.append(row)

max_num = input_list[0][0]
max_i = 0
max_j = 0
for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        if input_list[i][j] > max_num:
            max_num = input_list[i][j]
            max_i = i
            max_j = j

print(str(max_i) + " " + str(max_j))
