
def numbers_filter():

    list_of_strings = ['2', '3', '13', '17', '2', '8']

    to_filter_range = range(3)

    filtered_list = [number for number in list_of_strings if int(number)
                     not in to_filter_range]
    print(filtered_list)


if __name__ == '__main__':
    numbers_filter()
