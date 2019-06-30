import datetime


def get_today_date():
    return datetime.date.today().strftime('Today is %d,%b,%y')


def main():
    print(get_today_date())


if __name__ == '__main__':
    main()