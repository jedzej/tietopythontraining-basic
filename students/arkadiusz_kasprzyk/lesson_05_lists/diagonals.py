def diagonals(n, m=None):
    """
    n: int
        number of rows
    m: int
        number of columns; if None then m = n;

    Returns
    -------
    Matrix where on each diagonal is its distance from the main diagonal.

    Examples
    --------
    from random_matrix import print_table

    print_table(diagonals(5))
    print_table(diagonals(13))
    print_table(diagonals(4, 5))
    print_table(diagonals(9, 8))
    """
    if m is None:
        m = n
    res = []
    for r in range(n):
        row = []
        for c in range(m):
            row += [abs(r - c)]
        res += [row]
    return res
