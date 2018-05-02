from datetime import datetime


if __name__ == '__main__':
    current_datetime = datetime.now()
    future_datetime = datetime(year=2025, month=1, day=13)
    print((future_datetime - current_datetime).days)
