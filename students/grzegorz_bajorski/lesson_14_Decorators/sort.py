def sort(input_fun):
    def func_wrapper():
        return sorted(input_fun())

    return func_wrapper


@sort
def data_feeder():
    return [4, 2, 1, 3]


print(data_feeder() == [1, 2, 3, 4])
