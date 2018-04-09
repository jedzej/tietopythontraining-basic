def get_filtered_array(array, range):
    return [j for j in [int(i) for i in array] if j not in range]


if __name__ == '__main__':
    array = str(input('Enter list of integers: ')).split()
    filter_range = int(input('Enter range to filter: '))

    filtered_array = get_filtered_array(array, range(filter_range))

    print(filtered_array)