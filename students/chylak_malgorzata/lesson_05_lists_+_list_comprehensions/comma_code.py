spam = ['apples', 'bananas', 'tofu', 'cats']


def objects(list):
    new = " "
    for i in list:
        new = new + str(i)
        if list.index(i) == (len(list)-2):
            new = new + ", and "
        elif list.index(i) == (len(list)-1):
            new = new
        else:
            new = new + ', '
    return new

print(objects(spam))
