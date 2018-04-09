import random

def random_matrix_int(R = 5, C = 7, max=10, min=0):
    mtx = []
    for r in range(R):
        row = []
        for c in range(C):
            row += [random.randint(min,max)]
        mtx += [row]

    #print(mtx)
    return(mtx)

def print_table(table):
    for r in range(len(table)):
        print(table[r])

def swap_columns(matrix, i, j):
    for r in range(len(matrix)):
        matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
    return matrix

#%%

matrix = random_matrix_int()

print_table(matrix)
print("")
print_table(swap_columns(matrix, 0, 1))