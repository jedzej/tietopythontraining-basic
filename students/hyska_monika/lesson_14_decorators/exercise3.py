"""
Write @logged decorator using logger_wrapper
from lesson 6. Apply it to several functions
to demonstrate that it works
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


print(data_feeder())
print(data_feeder() == [1, 2, 3, 4])
