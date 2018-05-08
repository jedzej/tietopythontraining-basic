def swap_columns(matrix, i, j):
    """
    For given matrix swaps columns i, j.

    Parameters
    ----------
    matrix: list of lists (rows) each having the same length;
    i: int
        index of a column to swap with the column j
    j: int
        index of a column to swap with the column i

    Returns
    -------
    matrix with columns i, j swapped

    Examples
    --------
    from random_matrix import *

    matrix = random_matrix_int()
    print_table(matrix)
<<<<<<< HEAD
    print_table(swap_columns(matrix, 0, 1))
=======
    print_table(swap_columns())
>>>>>>> 03 on adziu/lesson_05_lists

    """
    for r in range(len(matrix)):
        matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
<<<<<<< HEAD
    return matrix
=======
    return matrix
>>>>>>> 03 on adziu/lesson_05_lists
