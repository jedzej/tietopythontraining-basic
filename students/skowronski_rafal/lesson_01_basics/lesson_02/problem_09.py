# Solves problem 09 - Clock face - 1


def calculate_hour_hand_angle():
    FULL_ANGLE = 360
    HOURS_PER_FULL_ANGLE = 12
    MINUTES_PER_HOUR = 60
    SECONDS_PER_HOUR = 60 * 60

    hours = int(input('Enter number of hours (H): '))
    minutes = int(input('Enter number of minutes (M): '))
    seconds = int(input('Enter number of seconds (S): '))

    total_hours = hours + \
        (minutes / MINUTES_PER_HOUR) + \
        (seconds / SECONDS_PER_HOUR)

    angle = (total_hours * FULL_ANGLE) / HOURS_PER_FULL_ANGLE

    print('\nHour hand angle: {0:.4f}'.format(angle))

if __name__ == '__main__':
    calculate_hour_hand_angle()
