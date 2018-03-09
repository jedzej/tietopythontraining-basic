def get_angle(minutes):
    angle = minutes % 30 * 12
    print('angle is {}'.format(angle))

if __name__ == '__main__':
    minutes = float(input())
    get_angle(minutes)