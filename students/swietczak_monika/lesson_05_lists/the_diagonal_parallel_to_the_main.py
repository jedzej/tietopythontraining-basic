n = int(input("Please enter a positive integer number: "))

a = [[abs(i - j) for j in range(n)] for i in range(n)]

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
