# Solves problem 10 - Lost card


def _main():
    set_size = int(input('Enter original set size (N): '))

    sum_of_cards = 0
    sum_total = set_size
    for i in range(1, set_size):
        remaining_card = int(input('Enter card number: '))
        sum_of_cards += remaining_card
        sum_total += i

    print('\nNumber of the lost card: {0}'.format(sum_total - sum_of_cards))


if __name__ == '__main__':
    _main()
