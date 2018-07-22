EXPECTED_RESULT = [1, 2, 3, 4]


def sort(func):
    def sort_data():
        unsorted_data = func()
        sorted_data = sorted(unsorted_data)
        return sorted_data
    return sort_data


@sort
def data_feeder():
    return [4, 2, 1, 3]


def main():
    result = data_feeder()
    if result == EXPECTED_RESULT:
        print("Great success!")


if __name__ == '__main__':
    main()
