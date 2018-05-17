# sum_all.py


def sum_all(*args):
    """
    Examples
    --------
    sum_all(1)              # 1
    sum_all(1, 2, 3, 4)     # 10
    sum_all(1., 2., 3.)     # 6.
    """
    s = 0
    for k in args:
        s += k
    return s
