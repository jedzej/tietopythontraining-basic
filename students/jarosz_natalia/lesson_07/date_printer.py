from datetime import datetime


def display_current_date():
    return datetime.now().date()


def main():
    print(display_current_date())


if __name__ == '__main__':
    main()
