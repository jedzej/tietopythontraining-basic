
def the_bowling_alley():

    pins, balls = [int(i) for i in input().split()]
    pins_line = ['I'] * pins

    for i in range(balls):
        left_pin, right_pin = [int(i) for i in input().split()]
        for j in range(left_pin - 1, right_pin):
            pins_line[j] = '.'

    print(''.join(pins_line))


if __name__ == '__main__':
    the_bowling_alley()
