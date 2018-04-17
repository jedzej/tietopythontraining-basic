def data_input():
    data_in = input().split(" ")
    result = []
    for i in data_in:
        result.append(int(i))
    return result


def filters(n, list_str):
    new_list = []
    for i in list_str:
        if i == n or i > n:
            new_list.append(i)
    return new_list


list_of_strings = data_input()
to_filter_range = int(input())
print(filters(to_filter_range, list_of_strings))
