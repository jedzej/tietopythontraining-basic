def how_many_is_greater(list_of_numbers):
    greater_index = 0

    for i in range(1, len(list_of_numbers) - 1):
        if list_of_numbers[i - 1] < list_of_numbers[i] > \
                list_of_numbers[i + 1]:
            greater_index += 1
    print(greater_index)


def main():
    user_numbers = [int(x) for x in input().split()]
    how_many_is_greater(user_numbers)


if __name__ == '__main__':
    main()
