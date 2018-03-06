def get_first_digit_of_the_decimal_point(num):
    first_decimal_digit = int(num * 10) % 10
    print(first_decimal_digit)


if __name__ == '__main__':
    number = float(input())
    get_first_digit_of_the_decimal_point(number)