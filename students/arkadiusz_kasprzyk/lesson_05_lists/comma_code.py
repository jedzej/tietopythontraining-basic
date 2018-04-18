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

    s = ''
    l = len(lst)

    if l > 0:
        s += str(lst[0])
        if l > 1:
            sep = [', '] * (l - 2) + [' and ']
            for k in range(l - 1):
                s += (sep[k] + str(lst[k + 1]))
    return s
