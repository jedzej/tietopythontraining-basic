def better_list(full_list):
    if len(full_list) == 0:
        print("list is empty!")
    elif len(full_list) == 1:
        print(full_list[0])
    else:
        print(', '.join(full_list[0:-1]) + ' and ' + full_list[-1])


if __name__ == '__main__':
    wrong_list = ['apples', 'bananas', 'tofu', 'cats']
    better_list(wrong_list)
    wrong_list = ['apples']
    better_list(wrong_list)
    wrong_list = []
    better_list(wrong_list)
