def get_factorial():
    input_number = int(input())
    factorial = 1

    for i in range(1, input_number + 1):
        factorial = factorial * i

    print(factorial)


if __name__ == '__main__':
    get_factorial()
