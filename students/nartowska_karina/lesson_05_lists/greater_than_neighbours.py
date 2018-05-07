def greather_than_neighbours(list_value):
    amount = 0
    for i in range(1, len(list_value) - 1):
        if list_value[i] > list_value[i + 1]:
            if list_value[i] > list_value[i - 1]:
                amount += 1
    return amount


def data():
    input_value = input().split()
    output_value = []
    for j in input_value:
        output_value.append(int(j))
    return output_value


def main():
    print("Enter a list value:")
    list_value = data()
    print(greather_than_neighbours(list_value))


if __name__ == "__main__":
    main()
