def how_many_is_greather(list_of_numbers):
    greather_index = 0

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] < list_of_numbers[i] > \
                list_of_numbers[i + 1]:
            greather_index += 1
    print(greather_index)


def main():
    a = [int(x) for x in input().split()]
    print(a)
    sample_list = [-9, 29, -100, 64, 26, 73, -96, 28, -92, 11, -14, -86, -54,
                   -67]
    how_many_is_greather(sample_list)


if __name__ == '__main__':
    main()
