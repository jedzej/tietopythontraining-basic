def main():
    if data_feeder() == [1, 2, 3, 4]:
        print("Sort decorator works")


def sort(func):
    def func_sorter():
        unsorted_list = func()
        sorted_list = sorted(unsorted_list)
        return sorted_list
    return func_sorter


@sort
def data_feeder():
    return [4, 2, 1, 3]


if __name__ == '__main__':
    main()
