def counter(a):
    count = 0
    for i in range(1, len(a) - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            count += 1
    print("Number of items greater than both neighbours:", count)


def main():
    list_of_numbers = [int(x) for x in input("Input list: ").split()]

    counter(list_of_numbers)


if __name__ == '__main__':
    main()
