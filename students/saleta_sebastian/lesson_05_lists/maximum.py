def get_maximum(row, col, values):
    maximum_value = values[0][0]
    max_row, max_col = 0, 0

    for i in range(row):
        for j in range(col):
            if values[i][j] > maximum_value:
                maximum_value = values[i][j]
                max_row, max_col = i, j

    return max_row, max_col


def main():
    rows, columns = [int(i) for i in input("input rows and columns: ").split()]
    fulfillment = [
        [int(j) for j in input("Input " + str(columns) + " values: ").split()]
        for i in range(rows)]
    print(get_maximum(rows, columns, fulfillment))


if __name__ == "__main__":
    main()
