from datetime import datetime


def date_printer(date):
    return "{:%Y-%m-%d %H:%M}".format(date)


def main():
    print("Time: " + date_printer(datetime.now()))


if __name__ == '__main__':
    main()
