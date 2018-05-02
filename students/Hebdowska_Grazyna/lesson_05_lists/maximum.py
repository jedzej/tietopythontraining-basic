def data_input():
    data_in = input().split(" ")
    result = []
    for i in data_in:
        result.append(int(i))
    return result


def matrix_input(m):
    result = []
    for i in range(m):
        result.append(data_input())
    return result


def maximum(m, n, marix):
    max_value = marix[0][0]
    max_position = [0, 0]
    for i in range(m):
        for j in range(n):
            if marix[i][j] > max_value:
                max_value = marix[i][j]
                max_position = [i, j]
    return max_position


numbers = data_input()
number_rows = numbers[0]
number_elements = numbers[1]
print(maximum(number_rows, number_elements, matrix_input(number_rows)))
