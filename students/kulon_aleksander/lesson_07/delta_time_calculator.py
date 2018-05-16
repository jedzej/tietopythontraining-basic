from datetime import datetime


def main():
    current_datetime = datetime.now()
    future_datetime = datetime(year=2099, month=10, day=26)
    print((future_datetime - current_datetime).days)


if __name__ == '__main__':
    main()
