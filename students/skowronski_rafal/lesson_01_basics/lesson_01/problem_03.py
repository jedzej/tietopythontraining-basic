# Prints greetings to the user


def print_greetings():
    user_name = input('Enter user name: ')

    print('Hello, {0}!'.format(user_name))

if __name__ == '__main__':
    print_greetings()
