def comma_code(elements):
    sentence = ''
    length = len(elements)
    for i in range(length):
        if i is length-1:
            sentence += 'and ' + elements[i]
        else:
            sentence += elements[i] + ', '
    return sentence


spam = ['apples', 'bananas', 'tofu', 'apples', 'bananas', 'tofu', 'apples', 'bananas', 'tofu']
result = comma_code(spam)
print(result)
