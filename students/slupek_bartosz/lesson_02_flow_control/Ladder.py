 height = int(input())
for row in range(height):
    for number in range(row + 1):
        print(number + 1, end='')
    print("")
