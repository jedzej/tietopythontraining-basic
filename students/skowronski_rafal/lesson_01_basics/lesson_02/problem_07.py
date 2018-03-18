# Solves problem 07 - Digital clock


def print_hours_and_minutes():
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    minutes_total = int(input(
        'Enter number of minutes passed since midnight: '))

    minutes_day = minutes_total % (MINUTES_PER_HOUR * HOURS_PER_DAY)

    minutes_on_display = minutes_day % MINUTES_PER_HOUR
    hours_on_display = minutes_day // MINUTES_PER_HOUR

    print('\nClock display: {0:02}:{1:02}'.format(
        hours_on_display, minutes_on_display))

if __name__ == '__main__':
    print_hours_and_minutes()
