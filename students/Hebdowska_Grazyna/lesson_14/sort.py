def sort(fun):
    def sort_fun_wrapper():
        list_to_sort = fun()
        list_to_sort.sort()
        return list_to_sort

    return sort_fun_wrapper()


@sort
def data_feeder():
    return [4, 2, 1, 3]


print(data_feeder)
