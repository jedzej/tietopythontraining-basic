def convert_to_comma_string(array):

    if len(array) == 0:
        return ''

    if len(array) == 1:
        return str(array[0])

    if len(array) == 2:
        return str(array[0]) + ', ' + str(array[1])

    array_length = len(array)
    return ''.join(
        ['{0}, '.format(array[i])
            for i in range(array_length)
            if i < array_length - 1] +
        ['and {0}'.format(array[-1])])
