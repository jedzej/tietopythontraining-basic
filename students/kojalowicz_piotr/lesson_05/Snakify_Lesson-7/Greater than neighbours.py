def greater_than_neighbours(list_value):
    number = 0
    for position in range(1, len(list_value)-1):
        if list_value[position - 1] < list_value[position] and list_value[position + 1] < list_value[position]:
            number += 1
    return number


def main():
    values = input()
    numbers = values.split()
    print(greater_than_neighbours(numbers))


if __name__ == '__main__':
    main()
