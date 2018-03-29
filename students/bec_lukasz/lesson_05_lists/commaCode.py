
list_one = ['1', '2', '3', '4']
list_two = ['me', 'myself', 'I']


def show_my_list(spam):

    my_string = ''

    for i in range(len(spam)):
        if i == len(spam)-2:
            sep = ' and '
            my_string += str(spam[i])
            my_string += sep
        elif i == len(spam)-1:
            sep = ''
            my_string += str(spam[i])
            my_string += sep
        else:
            sep = ', '
            my_string += str(spam[i])
            my_string += sep

    return my_string


print(show_my_list(list_one))
print(show_my_list(list_two))
print(show_my_list([1, 2, 3, 4, 5, 20]))
print(show_my_list([1.0001, 87.2, 2.433232, 45454.4, 23.5, 1.20]))
