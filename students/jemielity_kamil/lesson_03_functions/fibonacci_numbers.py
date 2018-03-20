def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


if __name__ == "__main__":
    first_number = float(input('a: '))
    second_number = int(input('n: '))
    print(power(first_number, second_number))
