from datetime import datetime
from time import time
from date_printer import date_printer


def main():
    print("Time: " + date_printer(datetime.fromtimestamp(time())))


if __name__ == '__main__':
    main()
