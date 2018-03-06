def get_days(kilometers_per_day,route_length):
    days = route_length / kilometers_per_day
    if not days % 1 == 0:
        days = days + 1
    print('Car can cover {} days'.format(days))


if __name__ == '__main__':
    kilometers_per_day = int(input())
    route_length = int(input())
    get_days(kilometers_per_day, route_length)