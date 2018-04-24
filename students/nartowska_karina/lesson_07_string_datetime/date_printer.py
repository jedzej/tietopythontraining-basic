import datetime


def date_printer():
    print(datetime.datetime.now())
    current_time = datetime.datetime.now()
    print("Current time:")
    print("{:%H:%M}".format(current_time))
    current_date = datetime.datetime.now()
    print("Current date:")
    print("{:%Y-%m-%d}".format(current_date))


def main():
    print("Full format:")
    date_printer()


if __name__ == "__main__":
    main()
