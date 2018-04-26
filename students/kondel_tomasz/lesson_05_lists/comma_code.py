def comma_code(list):
    ret = ""
    temp_list = []
    for item in list:
        temp_list.append(item)
        temp_list.append(", ")

    temp_list.pop()
    temp_list.insert(-1, " and ")

    for item in temp_list:
        ret += item
    return ret


spam = ['apples', 'bananas', 'tofu', 'cats']

print(comma_code(spam))
