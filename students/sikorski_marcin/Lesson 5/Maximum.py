n, m = [int(i) for i in input("Give me two integers representing the rows and columns (m×n), "
                                      "\nand subsequent m rows of n elements so I can find"
                                      "\nthe maximum: ").split()]

a = [[int(j) for j in input().split()] for i in range(n)]
highest_i, highest_j = 0, 0
maximum_at_the_moment = a[0][0]

for i in range(n):
    for j in range(m):
        if a[i][j] > maximum_at_the_moment:
            maximum_at_the_moment = a[i][j]
            best_i, best_j = i, j
print(highest_i, highest_j)