
def turn_list_into_string(list_to_change):

    if len(list_to_change) == 1:
        return list_to_change[0]

    return '{}, and {}'.format(', '.join(list_to_change[:-1]), list_to_change[-1])


if __name__ == '__main__':
    print(turn_list_into_string(['apples', 'bananas', 'tofu', 'cats']))
