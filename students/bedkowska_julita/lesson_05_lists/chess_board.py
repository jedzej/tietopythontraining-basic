def chess_board(rows, columns):
    matrix = []
    sign = '*'

    for i in range(rows):
        array = []
        sign = change_sign(sign)
        for j in range(columns):
            array.append(sign)
            sign = change_sign(sign)
        matrix.append(array)

    print(matrix)


def change_sign(sign):
    if sign == '.':
        sign = '*'
    else:
        sign = '.'
    return sign


rows = int(input("Give the number of rows: "))
columns = int(input("Give the number of columns: "))
chess_board(rows, columns)
