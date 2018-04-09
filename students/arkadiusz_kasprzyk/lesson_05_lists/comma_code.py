def comma_code( lst ):

    s = ''
    l = len(lst)

    if l > 0:

        s += lst[0]

        if l > 1:

            sep = [', '] * (l - 2) + [' and ']

            for k in range(l - 1):

                s += (sep[k] + lst[k + 1])

    return s

#spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
#print(comma_code(spam))