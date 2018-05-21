def chess_board(rows, columns):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if i % 2 != j % 2:
                row.append("*")
            else:
                row.append(".")
        board.append(row)
    print("Result:")
    return board


def data():
    input_value = input().split()
    output_value = []
    for j in input_value:
        output_value.append(int(j))
    return output_value


def main():
    print("Enter data:")
    list_value = data()
    rows = list_value[0]
    columns = list_value[1]
    matrix = chess_board(rows, columns)
    for i in range(rows):
        print(' '.join(matrix[i]))


if __name__ == "__main__":
    main()
