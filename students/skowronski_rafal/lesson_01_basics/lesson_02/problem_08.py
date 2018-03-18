# Solves problem 08 - Total cost


def print_price():
    CENTS_PER_DOLLAR = 100

    dollars_per_cake = int(input('Enter dollars number (A): '))
    cents_per_cake = int(input('Enter cents number (B): '))
    cakes_number = int(input('Enter number of cupcakes (N): '))

    total_cents_per_cake = (CENTS_PER_DOLLAR * dollars_per_cake) + \
        cents_per_cake

    total_cents = cakes_number * total_cents_per_cake

    dollars = total_cents // CENTS_PER_DOLLAR
    cents = total_cents % CENTS_PER_DOLLAR

    print('\nTotal price: {0}.{1:02}$'.format(dollars, cents))

if __name__ == '__main__':
    print_price()
