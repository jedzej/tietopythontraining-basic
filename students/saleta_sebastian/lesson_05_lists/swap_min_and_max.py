def swap_min_and_max(numbers):
    min_number = 0
    max_number = 0

    for i in range(len(numbers)):
        min_number = numbers[0]
        if numbers[i] > max_number:
            max_number = numbers[i]
        if numbers[i] < min_number:
            min_number = numbers[i]
    print([max_number], [min_number])


def main():
    sample_list = [2, 3, 4, 5]
    swap_min_and_max(sample_list)


if __name__ == '__main__':
    main()
