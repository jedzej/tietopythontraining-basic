# Write a function that takes a list value as an argument and returns a
# string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list
#  to the function would return 'apples, bananas, tofu, and cats'. But your
# function should be able to work with any list value passed to it.


def insert_commas(list_value):
    connected_string = ', '.join(list_value[:-1]) + ' and ' + list_value[-1]
    
    return connected_string


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']

    more_spam = [
        'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Croatia',
        'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania',
        'Russia', 'Serbia', 'Slovakia']

    ending_spam = ['Male', 'Female']

    print(insert_commas(spam))
    print(insert_commas(more_spam))
    print(insert_commas(ending_spam))


if __name__ == "__main__":
    main()
