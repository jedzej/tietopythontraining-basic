def get_sum_of_factorials():
    input_number = int(input())
    factorial = 1
    sum = 0
    for i in range(1, input_number + 1):
        factorial = factorial * i
        sum = sum + factorial

    print(sum)


if __name__ == '__main__':
    get_sum_of_factorials()
