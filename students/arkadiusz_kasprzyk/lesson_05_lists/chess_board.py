def rep(x, length=None, times=None):
<<<<<<< HEAD
    """
    Replicates x (list or tuple) to the given length or times many.

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
            n = length // len(x) + ( length % len(x) > 0 )
            x = x * n
            x = x[:length]
=======
    if length is None:
        if times is None:
            raise ValueError
        else:
            x = x * times
    else:
        n = length // len(x) + ( length % len(x) > 0 )
        x = x * n
        x = x[:length]
>>>>>>> 00 adziu/lesson_05_lists

    return x


<<<<<<< HEAD
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
    """
=======

def chess_board(m, n):
>>>>>>> 00 adziu/lesson_05_lists
    chb = []
    for r in range(m):
        if r % 2:
            chb += [list(rep("*.",n))]
        else:
            chb += [list(rep(".*",n))]
    return chb
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 2cb88f3c0db2358d339f5bf43f3ccfccec26c78f
=======


chb = chess_board(8,8)

for r in range(len(chb)):
    print("".join(chb[r]))


#for r in range(len(chb)):
#    for c in range(len(chb[r])):
#        print(chb[r][c], end='')
#    print("")
>>>>>>> 00 adziu/lesson_05_lists
