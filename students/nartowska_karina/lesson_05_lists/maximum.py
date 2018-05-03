def maximum(rows, columns, data_set):
    max_value = data_set[0][0]
    pos_max = [0, 0]
    for i in range(rows):
        for j in range(columns):
            if data_set[i][j] > max_value:
                max_value = data_set[i][j]
                pos_max = [i, j]
    return pos_max


def matrix(rows):
    result = []
    for i in range(rows):
        result.append(data())
    return result


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
    print(maximum(rows, columns, matrix(rows)))


if __name__ == "__main__":
    main()
