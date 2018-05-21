def filter(filter_range, list_value):
    result = []
    for i in list_value:
        if i > filter_range or i == filter_range:
            result.append(i)
    return result


def data():
    input_value = input().split()
    output_value = []
    for j in input_value:
        output_value.append(int(j))
    return output_value


def main():
    print("Enter a list value:")
    list_value = data()
    print("Enter filter:")
    filter_range = int(input())
    print(filter(filter_range, list_value))


if __name__ == "__main__":
    main()
