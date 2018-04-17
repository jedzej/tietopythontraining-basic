def chess_board():
    n, m = [int(s) for s in input().split()]
    array = []
    string_result = ''
    for i in range(n):
        array.append(['*'] * m)
        for j in range(m):
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                array[i][j] = "."
        string_result += ' '.join(array[i]) + '\n'
    return string_result


result = chess_board()
print(result)
