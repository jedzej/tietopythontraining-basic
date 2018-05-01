n = int(input("Number: "))

for i in range(1, n + 1):
    for l in range(1, i + 1):
        print(l, sep='', end='')
    print()
