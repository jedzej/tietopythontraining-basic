from datetime import datetime


def main():
    print("{:%Y-%m-%d %H:%M}".format(datetime.now()))


if __name__ == '__main__':
    main()
