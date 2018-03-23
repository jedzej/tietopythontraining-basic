def get_sum_of_factorials():
    input_number = int(input())
    factorial = 1
    summary = 0

    for i in range(1, input_number + 1):
        factorial = factorial * i
        summary = summary + factorial

    print(summary)


if __name__ == '__main__':
    get_sum_of_factorials()
