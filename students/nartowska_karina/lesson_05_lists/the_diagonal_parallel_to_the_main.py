def diagonal_parallel(size):
    matrix_image = []
    for i in range(size):
        row = []
        for j in range(size):
            if i < j:
                row.append(j - i)
            else:
                row.append(i - j)
        matrix_image.append(row)
    print("Result:")
    return matrix_image


def main():
    print("Enter size:")
    size = int(input())
    matrix = diagonal_parallel(size)
    for i in range(size):
        print(''.join(str(matrix[i])))


if __name__ == "__main__":
    main()
