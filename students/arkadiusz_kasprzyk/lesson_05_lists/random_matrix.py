"""
random_matrix

Generator of random matrix == list of lists (rows),
all sublists of the same length.
Also a function to print such matrices (each row (sublist)
in a separate line).
Currently only integer values.

Examples
--------
print_table(random_matrix_int(5, 7))
print_table(random_matrix_int(5, 7, 20))
print_table(random_matrix_int(5, 7, 20, 10))
"""

import random


def random_matrix_int(R=5, C=7, max=9, min=0):
    """
    Parameters
    ----------
    R: int
        number of rows
    C: int
        number of columns (row length)
    max: int
        upper limit of integers set from which values are sampled
    min:
        lower limit of integers set from which values are sampled

    Returns
    -------
        matrix of size R x C
        == list of lists (rows), R rows, each row of length C;
        values sampled from the integer set [min, max] by random.randint()
    """
    mtx = []
    for r in range(R):
        row = []
        for c in range(C):
            row += [random.randint(min, max)]
        mtx += [row]

    return(mtx)


def print_table(table):
    for r in range(len(table)):
        print(table[r])
