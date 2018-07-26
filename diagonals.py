n = int(input())
array = []
for i in range(n):
    array.append([])
    for j in range(n):
        array[i].append(abs(i - j))
for row in array:
    print(' '.join(str(i) for i in row))