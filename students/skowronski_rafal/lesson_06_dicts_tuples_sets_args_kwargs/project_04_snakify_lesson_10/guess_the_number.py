import random
import enum


class ActionType(enum.Enum):
    HELP = 1,
    GUESS = 2


def print_set(set_to_print):
    print(' '.join([str(i) for i in set_to_print]))


def read_input_data():
    input_string = input()
    if (input_string == 'HELP'):
        return dict(action_type=ActionType.HELP)
    return dict(
        action_type=ActionType.GUESS,
        values=set([int(i) for i in input_string.split()]))


def play_the_game(set_len, target_number):
    remaning_set = set(range(1, set_len + 1))

    while True:
        input_data = read_input_data()
        if input_data['action_type'] == ActionType.GUESS:
            values = input_data['values']
            if target_number in values:
                remaning_set = values
                print('YES')
                if len(values) == 1:
                    break
            else:
                remaning_set -= values
                print('NO')
        else:
            print_set(remaning_set)


if __name__ == '__main__':
    set_len = int(input('Enter range (n): '))
    target_number = random.randint(1, set_len)

    play_the_game(set_len, target_number)
