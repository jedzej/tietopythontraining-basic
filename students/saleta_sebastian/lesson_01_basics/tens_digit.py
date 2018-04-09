def get_tens_digit():
    number = int(input())
    tens_digit = number // 10 % 10
    print ('Tens digit is {}.'.format(tens_digit))


if __name__ == '__main__':
    get_tens_digit()
