def statement():
    first_number = int(input('Please write intiger number:\n'))
    second_number = int(input('Please Write another intiger number:\n'))
    if first_number > second_number:
        print('The smaller number is: ', second_number)
    elif first_number < second_number:
        print('The smaller number is: ', first_number)
    else:
        print('Both numbers are same', first_number, '', second_number)


if __name__ == '__main__':
    # statement()
    pass