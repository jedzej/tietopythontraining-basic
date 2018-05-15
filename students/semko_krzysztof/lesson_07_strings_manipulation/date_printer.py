"""
Date printer - write a script that displays
current date in human-readable format
"""
from datetime import datetime


def main():
    print(datetime.now().strftime('%Y.%m.%d %H:%M'))


if __name__ == '__main__':
    main()
