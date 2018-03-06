def calc_angle():
    hours = int(input())
    minutes = int(input())
    seconds = int(input())
    angle = ((hours * 30) + (minutes * 30 / 60) + (seconds * 30 / 3600))

    print(angle)


if __name__ == '__main__':
    calc_angle()
