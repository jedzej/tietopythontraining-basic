from statistics import mean


def get_adults_average_age(array):
    return _get_avarage_on_condition(array, lambda age: age >= 18)


def get_children_average_age(array):
    return _get_avarage_on_condition(array, lambda age: age < 18)


def _get_avarage_on_condition(array, condition):
    filtered_array = [i for i in array if condition(i)]
    if len(filtered_array) == 0:
        return None
    return mean(filtered_array)


if __name__ == '__main__':
    array = [int(i) for i in str(input('Enter list of ages: ')).split()]

    print('Average age of adults: {0}'
          .format(get_adults_average_age(array)))

    print('Average age of children: {0}'
          .format(get_children_average_age(array)))
