def swap_min_and_max(items):
    index_min = items.index(min(items))
    index_max = items.index(max(items))
    items[index_max], items[index_min] = items[index_min], items[index_max]
    print(' '.join([str(item) for item in items]))


def main():
    numbers = [int(number)
               for number in input("List of numbers: ").split()]

    swap_min_and_max(numbers)


if __name__ == '__main__':
    main()
