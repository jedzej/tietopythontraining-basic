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

