def main():
    numbers = [int(x) for x in input().split()]
    quantity = 0
    for x in range(1, len(numbers) - 1):
        if numbers[x] > numbers[x - 1] and numbers[x] > numbers[x + 1]:
            quantity += 1

    print(quantity)


if __name__ == '__main__':
    main()
