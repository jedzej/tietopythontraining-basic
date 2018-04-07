def swap(array):

    tmp_array = [int(i) for i in array]
    min_index = tmp_array.index(min(tmp_array))
    max_index = tmp_array.index(max(tmp_array))

    tmp = array[min_index]
    array[min_index] = array[max_index]
    array[max_index] = tmp


if __name__ == '__main__':
    elements = str(input('Enter elements separated by space: ')).split()
    swap(elements)
    print('Swapped array: {0}'
          .format(''.join(['{0} '.format(i) for i in elements])))
