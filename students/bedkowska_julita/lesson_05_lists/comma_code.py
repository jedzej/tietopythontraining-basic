def commaCode(list):
    result = ''
    for i in range(len(list) - 1):
        result = result + list[i] + ', '
    result = result + 'and ' + list[-1] + '.'
    return result


spam = ['apples', 'bananas', 'tofu', 'cats']
print('Input list: ' + str(spam))
print('Result: ' + commaCode(spam))
