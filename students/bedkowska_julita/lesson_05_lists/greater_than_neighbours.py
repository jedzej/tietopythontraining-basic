def greater_than_neighbours(list):
    result = 0
    for i in range(1, len(list) - 1):
        if list[i] > list[i-1] and list[i] > list[i+1]:
            result += 1
    return result


test = [-9, 29, -100, 64, 26, 73, -96, 28, -92, 11, -14, -86, -54, -67]
print(greater_than_neighbours(test))
