def previous_and_next():
    number = int(input())
    number_one_more = number + 1
    number_one_less = number - 1
    print('The next number for the number {} is {}'
          .format(number, number_one_more))
    print('The previous number for the number {} is {}'
          .format(number, number_one_less))


if __name__ == '__main__':
    previous_and_next()
