from random_matrix import *
from swap_columns import *

#matrix = random_matrix_int()
matrix = random_matrix_int(4, 4, 1)


print_table(matrix)
print()
#print_table(swap_columns(matrix, 0, 1))
print_table(swap_columns(matrix, 3, 1))
