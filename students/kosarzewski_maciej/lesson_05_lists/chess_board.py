m, n = [int(x) for x in input().split()]
# board = []
for i in range(m):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(".", end=" ")
        else:
            print("*", end=" ")
        if j == n - 1:
            print()
