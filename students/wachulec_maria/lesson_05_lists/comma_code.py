def comma_code(some_list):
    result = ''
    for i in range(len(some_list)-1):
        result = result + some_list[i] + ', '
    result = result + 'and ' + some_list[-1] + '.'
    return result


spam = ['apples', 'bananas', 'tofu', 'cats']
output = comma_code(spam)
print(output)
