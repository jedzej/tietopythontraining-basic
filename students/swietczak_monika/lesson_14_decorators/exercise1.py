def sort(some_function):
    def sort_list():
        return sorted(some_function())

    return sort_list


@sort
def data_feeder():
    return [4, 2, 1, 3]


print(data_feeder() == [1, 2, 3, 4])  # <- this is True
