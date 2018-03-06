def get_fractional_part_of_num(num):
    fractional = float(num) % 1.0
    print('Fractional part is {}'.format(fractional))


if __name__ == '__main__':
    number = raw_input()
    get_fractional_part_of_num(number)