def main():
    result = data_feeder()
    if result == [1, 2, 3, 4]:
        print("well sorted!")


def sort(func):
    def sort_data():
        unsorted_data = func()
        sorted_data = sorted(unsorted_data)
        return sorted_data
    return sort_data


@sort
def data_feeder():
    return [4, 2, 1, 3]


if __name__ == '__main__':
    main()
