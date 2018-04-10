def numbers_filter(string_list, range_list):
    final_list = []
    for element in string_list:
        if int(element) not in range_list:
            final_list.append(int(element))
    return final_list


def main():
    string_list = ['1', '2', '0', '8', '3', '2', '7']
    range_list = range(3)
    range_list = list(range_list)
    print(numbers_filter(string_list, range_list))


if __name__ == "__main__":
    main()
