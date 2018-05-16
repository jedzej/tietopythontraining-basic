from datetime import datetime


def get_current_date():
    return datetime.now().date()


def main():
    print(get_current_date())


if __name__ == '__main__':
    main()
