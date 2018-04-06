<<<<<<< HEAD
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

=======
import random

def random_matrix_int(R = 5, C = 7, min=0, max=100):
    mtx = []
    for r in range(R):
        row = []
        for c in range(C):
            row += [random.randint(min,max)]
        mtx += [row]

    print(mtx)
    return(mtx)

def maximum(mtx):
    maxi = 0
    idx = [0, 0]
    for r in range(len(mtx)):
        for c in range(len(mtx[0])):
            if maxi < mtx[r][c]:
                maxi = mtx[r][c]
                idx = [r, c]
    return maxi, idx

print(maximum(random_matrix_int(5, 7, 0, 100)))

>>>>>>> 00 adziu/lesson_05_lists
