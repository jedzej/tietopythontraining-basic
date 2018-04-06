<<<<<<< HEAD
<<<<<<< HEAD
def comma_code(lst):
=======
def comma_code( lst ):
>>>>>>> 2cb88f3c0db2358d339f5bf43f3ccfccec26c78f
    """
    Parameters
    ----------
    lst: list

    Returns
    -------
    string constructed from elements of the `lst` by joining them with ', '
    and the last two with ' and '.

    Examples
    --------
    print(comma_code(['apples', 'bananas', 'tofu', 'cats', 'dogs']))
    print(comma_code(['apples', 'bananas', 'tofu']))
    print(comma_code(['apples', 'bananas']))
    print(comma_code(['apples']))
    print(comma_code([]))
    """

<<<<<<< HEAD
    string = ''
    length = len(lst)

    if length > 0:
        string += str(lst[0])
        if length > 1:
            sep = [', '] * (length - 2) + [' and ']
            for k in range(length - 1):
                string += (sep[k] + str(lst[k + 1]))
    return string


"""
# alternatively:

if len(lst) > 1:
    *all_but_last, last = lst   # !!!
    return ', '.join(all_but_last) + ', and ' + last
else:
  return lst
"""
=======
    s = ''
    l = len(lst)

    if l > 0:
        s += str(lst[0])
        if l > 1:
            sep = [', '] * (l - 2) + [' and ']
            for k in range(l - 1):
                s += (sep[k] + str(lst[k + 1]))
    return s



>>>>>>> 2cb88f3c0db2358d339f5bf43f3ccfccec26c78f
=======
def comma_code( lst ):

    s = ''
    l = len(spam)

    if l > 0:

        s += lst[0]

        if l > 1:

            sep = [', '] * (l - 2) + [' and ']

            for k in range(l-1):

                s += (sep[k] + lst[k+1])

    return s

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']

print(comma_code(spam))
>>>>>>> 00 adziu/lesson_05_lists
