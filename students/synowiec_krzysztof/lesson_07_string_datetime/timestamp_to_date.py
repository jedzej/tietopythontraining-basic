from datetime import datetime


def main():
    timestamp = float(input("Provide timestamp: "))
    print("{:%Y-%m-%d %H:%M}".format(datetime.fromtimestamp(timestamp)))


if __name__ == '__main__':
    main()
