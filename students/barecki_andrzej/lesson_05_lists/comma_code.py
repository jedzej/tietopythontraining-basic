def coma_code(my_list):
    string_computing = ''
    while True:
        if len(my_list) > 1:
            string_computing += my_list[0] + ', '
            del my_list[0]
        else:
            string_computing += 'and ' + my_list[0]
            break
    return string_computing


spam = ['apples', 'bananas', 'tofu', 'cats']
print(coma_code(spam))
