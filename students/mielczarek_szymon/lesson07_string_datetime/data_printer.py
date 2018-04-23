from datetime import datetime


def get_current_date():
    return datetime.now().date()


if __name__ == '__main__':
    print(get_current_date())
