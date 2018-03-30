def get_first_digit_of_the_decimal_point():
    num = float(input())
    first_decimal_digit = int(num * 10) % 10
    print('first decimal digit is {}'.format(first_decimal_digit))


if __name__ == '__main__':
    get_first_digit_of_the_decimal_point()
