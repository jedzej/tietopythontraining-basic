def main():
    numbers = [int(x) for x in input().split()]
    min_ind = 0
    max_ind = 0
    for x in range(1, len(numbers)):
        if numbers[x] > numbers[max_ind]:
            max_ind = x
        elif numbers[x] < numbers[min_ind]:
            min_ind = x

    numbers[max_ind], numbers[min_ind] = numbers[min_ind], numbers[max_ind]
    for x in range(len(numbers)):
        print(numbers[x], end=" ")


if __name__ == '__main__':
    main()
