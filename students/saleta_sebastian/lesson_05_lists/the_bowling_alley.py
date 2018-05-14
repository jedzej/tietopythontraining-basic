def bowl(balls, pins):
    pins_table = ['I'] * pins
    print(pins_table)
    for j in range(balls):
        left, right = [int(k) for k in input().split()]
        for pin in range(left - 1, right):
            pins_table[pin] = '.'
    print(''.join([i for i in pins_table]))


def main():
    user_pins, user_balls = [int(i) for i in input().split()]

    bowl(user_balls, user_pins)


if __name__ == '__main__':
    main()
