def numbers_filter():

    list = ['1', '2', '3', '6', '7',' 8', '14', '17']

    to_filter = range(4)

    filtered = [number for number in list if int(number) not in to_filter]

    print(filtered)


if __name__ == '__main__':
    numbers_filter()
