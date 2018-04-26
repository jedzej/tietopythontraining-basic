age_list = [1, 35, 65, 13, 18, 34, 76, 4, 8, 6, 45, 34]


def filters(list_values, list_filter):
    val_position = 0
    while val_position < len(list_values):
        if list_values[val_position] in list_filter:
            list_values.remove(list_values[val_position])
        else:
            val_position += 1
    return list_values


def calculate_age(input_list):
    adults_list = list(x for x in input_list if x >= 18)
    # children_list = list(x for x in input_list if x < 18)
    children_list = filters(input_list, adults_list)
    return sum(adults_list) / len(adults_list), len(children_list)


print(calculate_age(age_list))
