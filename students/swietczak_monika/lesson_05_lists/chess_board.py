m, n = [int(s) for s in
        input("Enter two integer numbers with space between them: ").split()]
for i in range(m):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(".", end=" ")
        else:
            print("*", end=" ")
        if j == n - 1:
            print("")
