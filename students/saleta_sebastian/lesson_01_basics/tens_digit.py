def get_tens_digit(number):
    tens_digit = number // 10 % 10
    print ('Tens digit is {}.'.format(tens_digit))

if __name__ == '__main__':
    number = int(input())
    get_tens_digit(number)