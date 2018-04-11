from random_matrix import *
from maximum import *

#mtx = random_matrix_int(5, 5)
#mtx = random_matrix_int(5, 5, 99, 10)
mtx = random_matrix_int(5, 5, 3, -3)

print_table(mtx)
print(maximum(mtx))
