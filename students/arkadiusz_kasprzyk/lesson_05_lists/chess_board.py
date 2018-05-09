def rep(x, length=None, times=None):
    """
    Replicate sequence (list or tuple) to the given length or times many.

    Parameters
    ----------
    x: list or tuple
    length: int >= 0
    times: int

    Returns
    -------
    x replicated to the given length or times many.
    """
    if length is None:
        if times is None:
            raise TypeError
        else:
            x = x * times
    else:
        if length < 0:
            raise ValueError
        else:
            n = length // len(x) + (length % len(x) > 0)
            x = x * n
            x = x[:length]

    return x


def chess_board(m, n):
    """
    Parameters
    ----------
    m: int > 0
        number of rows
    n: int > 0
        number of columns

    Returns
    -------
    Chessboard made of '.' and '*' of size m x n.

    Examples
    --------
    from random_matrix import print_table

    chb = chess_board(7,8)
    print_table(chb)

    for r in range(len(chb)):
        print("".join(chb[r]))
    """

    chb = []
    for r in range(m):
        if r % 2:
            chb += [list(rep("*.", n))]
        else:
            chb += [list(rep(".*", n))]
    return chb
