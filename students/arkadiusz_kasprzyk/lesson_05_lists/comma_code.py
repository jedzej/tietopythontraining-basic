def comma_code(lst):
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
