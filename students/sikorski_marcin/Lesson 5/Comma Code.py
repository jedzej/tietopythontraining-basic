spam = ['apples', 'bananas', 'tofu', 'cats']

def printing_list(list_to_check):
    for x in list_to_check[:-1]:
        print(x, end=", ")
    print("and " + list_to_check[-1])

printing_list(spam)