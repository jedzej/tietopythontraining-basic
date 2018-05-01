def matrix(n):
    new_array = []
    for i in range(n):
        new_array_row = []
        for j in range(n):
            if i > j:
                new_array_row.append(i - j)
            else:
                new_array_row.append(j - i)
        new_array.append(new_array_row)

    return new_array


n = int(input())
array = matrix(n)
for i in range(n):
    print(''.join(str(array[i])))
