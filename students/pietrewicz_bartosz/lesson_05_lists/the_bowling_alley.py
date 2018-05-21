

def main():
    pins, balls = [int(x) for x in input().split()]
    pin_status = ['I'] * pins
    for i in range(balls):
        start_pin, end_pin = [int(x) for x in input().split()]
        for j in range(start_pin - 1, end_pin):
            pin_status[j] = '.'
    print(''.join(pin_status))


if __name__ == '__main__':
    main()
