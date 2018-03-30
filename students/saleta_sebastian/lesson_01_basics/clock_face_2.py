def get_angle():
    minutes = float(input())
    angle = minutes % 30 * 12
    print('angle is {}'.format(angle))


if __name__ == '__main__':
    get_angle()
