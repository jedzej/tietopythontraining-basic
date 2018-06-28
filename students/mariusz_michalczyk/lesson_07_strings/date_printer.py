from datetime import datetime


if __name__ == '__main__':
    now = datetime.now()
    print("Today is: ")
    print(now.strftime("%d %B of %Y year"))
