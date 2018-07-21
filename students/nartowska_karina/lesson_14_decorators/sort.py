def sort(func):
    def func_wrapper():
        sorted_list = func()
        sorted_list.sort()
        return sorted_list

    return func_wrapper()


@sort
def data_feeder():
    return [4, 2, 1, 3]


print(data_feeder)
