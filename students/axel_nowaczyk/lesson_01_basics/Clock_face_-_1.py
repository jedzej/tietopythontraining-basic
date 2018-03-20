from decimal import Decimal


def clock_face():
    hours = Decimal(input())
    minutes = Decimal(input())
    seconds = Decimal(input())

    print(((seconds/60 + minutes)/60 + hours)*360/12)


if __name__ == '__main__':
    clock_face()