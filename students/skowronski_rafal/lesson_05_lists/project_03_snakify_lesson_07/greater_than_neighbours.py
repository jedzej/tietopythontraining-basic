def get_number_of_elements(array):

    array_length = len(array)
    if array_length == 0 or array_length == 1 or array_length == 2:
        return 0

    number = 0
    for i in range(1, array_length - 1):
        if float(array[i - 1]) < float(array[i]) \
                and float(array[i]) > float(array[i + 1]):
            number += 1

    return number


if __name__ == '__main__':
    elements = str(input('Enter elements separated by space: ')).split()
    print('Number of elements: {0}'
          .format(get_number_of_elements(elements)))
