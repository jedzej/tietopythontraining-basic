"""

def sort(func):
    def func_wrapper(list):
        list.sort()
        return list
    return func_wrapper


@sort
def data_feeder(list):
    return list
"""
def sort(func):
    def func_wrapper():
        my_list = func()
        my_list.sort()
        return my_list
    return func_wrapper


@sort
def data_feeder():
    return [2, 1, 3, 4]
"""
mylist = [2, 1, 3, 4]
print(data_feeder(mylist))
print(data_feeder(mylist) == [1, 2, 3, 4])
"""
#print(data_feeder())
print(data_feeder() == [1, 2, 3, 4])
