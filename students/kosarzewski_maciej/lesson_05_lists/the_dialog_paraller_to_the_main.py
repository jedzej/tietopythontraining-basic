size = int(input())
for x in range(size):
    for y in range(size):
        print(str(abs(x - y)), end=" ")
    print("")
