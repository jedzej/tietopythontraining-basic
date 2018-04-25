def comma(user_list):
    if user_list == []:
        print('the list is empty')
        return user_list

    if len(user_list) == 1:
        return ''.join(user_list)

    else:
        user_list.insert(len(user_list) - 1, 'and')
        string_from_list = ', '.join(user_list)
        return string_from_list


def main():
    input_list = [str(x) for x in input().split()]

    print(comma(input_list))


if __name__ == '__main__':
    main()
