# sum_all.py


def sum_all(*args):
    """
    Examples
    --------
<<<<<<< HEAD
    sum_all(1)              # 1
    sum_all(1, 2, 3, 4)     # 10
    sum_all(1., 2., 3.)     # 6.
=======
    sum_all(1)
    sum_all(1, 2, 3, 4)
    sum_all(1., 2., 3.)
>>>>>>> 20508ca4668bf458c74a7d554f4bab5ad0bf3736
    """
    s = 0
    for k in args:
        s += k
    return s
