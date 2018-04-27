# Given a list of unique numbers, swap the minimal and maximal elements of
# this list. Print the resulting list.


def swap_min_max(list_value):
    max_idx = list_value.index(max(list_value))
    min_idx = list_value.index(min(list_value))

    list_value[max_idx], list_value[min_idx] = \
        list_value[min_idx], list_value[max_idx]

    return list_value


def main():
    test = [1, 5, 4, 3, 2]
    print(swap_min_max(test))

    test = [
        13, 14, 15, 16, 17,
        18, 17, 16, 15, 14]
    print(swap_min_max(test))


if __name__ == "__main__":
    main()
