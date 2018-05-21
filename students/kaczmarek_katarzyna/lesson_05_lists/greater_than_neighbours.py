def count_greater_than_neighbours(numbers):
    counter = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            counter += 1
    print("Number of items greater than both neighbours:", counter)


def main():
    numbers = [int(number)
               for number in input("List of numbers: ").split()]

    count_greater_than_neighbours(numbers)


if __name__ == '__main__':
    main()
