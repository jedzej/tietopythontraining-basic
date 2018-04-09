def print_matrix_as_string(matrix):
    print(end='\n')
    print('\n'.join([' '.join([str(elem) for elem in row]) for row in matrix]))
