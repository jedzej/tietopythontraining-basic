def factorials():
    sum = 0
    last_factorial = 1
    max_number = int(input())
    for i in range(1, max_number+1):
        last_factorial *= i
        sum += last_factorial
    print(sum)


if __name__ == '__main__':
    factorials()