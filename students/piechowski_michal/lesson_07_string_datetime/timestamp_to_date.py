#!/usr/bin/env python3

import datetime


def main():
    print(datetime.datetime.fromtimestamp(1234567890).strftime('%d.%m.%Y'))


if __name__ == "__main__":
    main()
