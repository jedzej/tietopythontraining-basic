

def str_to_int_filter(l, flt):
    return [int(x) for x in l if int(x) not in flt]


def main():
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)
    print(str_to_int_filter(list_of_strings, to_filter_range))


if __name__ == '__main__':
    main()
