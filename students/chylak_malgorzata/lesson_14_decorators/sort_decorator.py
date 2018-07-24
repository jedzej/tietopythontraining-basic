def sort(function):
    def list_sort():
        return sorted(function())
    return list_sort


@sort
def data_feeder():
    return [4,2,1,3]


print(data_feeder())
