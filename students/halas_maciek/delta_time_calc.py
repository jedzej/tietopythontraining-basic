from datetime import datetime


def print_delta_time(future_date):
    today_date = datetime.now()
    print(today_date)
    delta = future_date - today_date
    print('DELTA TIME: {}'.format(delta))


def main():
    date_from_future = datetime(2033, 12, 23)
    print_delta_time(date_from_future)


if __name__ == '__main__':
    main()