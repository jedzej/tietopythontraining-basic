def sort_decorator(func):
    def func_wrapper():
        received_list = func()
        received_list.sort()
        print('Original list', received_list)
        return received_list

    return func_wrapper


@sort_decorator
def data_feeder():
    return [4, 2, 1, 3]


if data_feeder() == [1, 2, 3, 4]:
    print('List has been sorted correctly')
else:
    print('List has not been sorted correctly')
