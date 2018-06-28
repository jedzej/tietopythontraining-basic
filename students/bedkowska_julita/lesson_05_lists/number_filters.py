def number_filters(list, max):
    result = []
    for i in range(len(list)):
        element = int(list[i])
        if element >= max:
            result.append(element)
    print(result)
    return result


list_of_strings = ['2', '0', '8', '3']
range1 = 3
number_filters(list_of_strings, range1)
