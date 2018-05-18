# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and
# returns a string with all the items separated by a comma and
# a space, with and inserted before the last item. For example,
# passing the previous spam list to the function would return
# 'apples, bananas, tofu, and cats'. But your function should
# be able to work with any list value passed to it.

def list_to_string(lista):
    lista.insert(-1, 'and')
    new_string = ', '.join(lista[:-1]) + ' ' + lista[-1]
    return new_string


if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(list_to_string(spam))
