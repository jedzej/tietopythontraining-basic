def sort(func):
    def func_wrapper():
        return sorted(func())
    return func_wrapper


@sort
def data_feeder():
    return [4, 2, 1, 3]


def main():
    if data_feeder() == [1, 2, 3, 4]:
        print("Decorator @sort works fine")
    else:
        print("Decorator @sort does not work!")


if __name__ == '__main__':
    main()
