def maximum(matrix):
    """
    Finding maximum of the matrix.

    Parameters
    ----------
    matrix: list of lists (rows) of int
        each row has the same length

    Returns
    -------
    maximum: maximum value of a matrix
    [r, c]: indices of the maximum.

    Examples
    --------
    from random_matrix import *

    mtx = random_matrix_int(5, 5)
    mtx = random_matrix_int(5, 5, 20)
    mtx = random_matrix_int(5, 5, 2, -2)

    print_table(mtx)
    print(maximum(mtx))
    """

    maxi = 0        # initial maximum
    idx = [0, 0]    # initial indices
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if maxi < matrix[r][c]:
                maxi = matrix[r][c]
                idx = [r, c]
    return maxi, idx
