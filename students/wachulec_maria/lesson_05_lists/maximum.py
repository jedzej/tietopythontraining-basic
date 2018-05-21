def maximum():
    m, n = [int(s) for s in input().split()]
    sample_list = [[0] * n] * m
    indexes = [0, 0]
    for row in range(len(sample_list)):
        sample_list[row] = [int(s) for s in input().split()]
        for element in range(len(sample_list[row])):
            if sample_list[row][element] > sample_list[indexes[0]][indexes[1]]:
                indexes = [row, element]
    return str(indexes[0]) + ' ' + str(indexes[1])


result = maximum()
print(result)
