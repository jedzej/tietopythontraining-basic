from datetime import datetime


def main():
    y, m, d = [int(x) for x in input().split()]
    custom_date = datetime(year=y, month=m, day=d)
    current_date = datetime.now()
    print((current_date - custom_date).days)


if __name__ == '__main__':
    main()
