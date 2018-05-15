def swap_min_and_max(list_value):
    pos_max = 0
    pos_min = 0
    max_value = list_value[0]
    min_value = list_value[0]
    for i in range(1, len(list_value)):
        if min_value > list_value[i]:
            min_value = list_value[i]
            pos_min = i
        if max_value < list_value[i]:
            max_value = list_value[i]
            pos_max = i
    list_value[pos_max] = min_value
    list_value[pos_min] = max_value
    print("Result:")
    return list_value


def data():
    input_value = input().split()
    output_value = []
    for j in input_value:
        output_value.append(int(j))
    return output_value


def main():
    print("Enter a list value:")
    list_value = data()
    print(swap_min_and_max(list_value))


if __name__ == "__main__":
    main()
