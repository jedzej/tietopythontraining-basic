# Solves problem 06 - Car route


def calculate_number_of_days():
    distance_per_day = int(input('Enter kilometers per day: '))
    route_length = int(input('Enter route distance: '))

    print('\nDays needed to cover the distance: {0}'.format(
        route_length / distance_per_day))
    print('Whole number of days needed to cover the distance: {0}'.format(
        -(-route_length // distance_per_day)
    ))

if __name__ == '__main__':
    calculate_number_of_days()
