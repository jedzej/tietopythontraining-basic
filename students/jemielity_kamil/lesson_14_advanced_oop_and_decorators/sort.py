def sort(func):
    def function_wrapper():
        return sorted(func())
    return function_wrapper


@sort
def data_feeder():
    return [4, 2, 1, 3]


print(data_feeder())
