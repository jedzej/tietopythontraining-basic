def comma_code(list):
    output = ''
    for i in range(len(list) - 1):
        output += (list[i]) + ', '
    return output + 'and ' + list[-1]


print(comma_code((input().split())))