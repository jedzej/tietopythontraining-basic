import datetime


def timestamp_to_date(timestamp):
    print(datetime.datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y'))
    print(datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M'))


def main():
    print("Enter unix timestamp:")
    timestamp = int(input())
    print("Result:")
    timestamp_to_date(timestamp)


if __name__ == "__main__":
    main()
