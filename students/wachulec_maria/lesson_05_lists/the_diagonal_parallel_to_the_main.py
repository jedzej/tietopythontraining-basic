def diagonal_matrix():
    result = []
    for i in range(n):
        working = []
        for j in range(n):
            working.append(abs(j - i))
        result.append(working)
    return result


def show_matrix(list_of_list):
    for r in list_of_list:
        print(' '.join([str(elem) for elem in r]))


n = int(input())
result_matrix = diagonal_matrix()
show_matrix(result_matrix)
