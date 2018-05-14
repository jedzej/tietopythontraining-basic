"""
Timestamp to date - write a script that converts
unix timestamp to human-readable date format
"""
from datetime import datetime
from time import time


def main():
    timestamp = time()
    print(datetime.fromtimestamp(timestamp).strftime('%Y.%m.%d %H:%M'))


if __name__ == '__main__':
    main()
