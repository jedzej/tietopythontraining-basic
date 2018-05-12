def knock(pins, balls):
    result = ['I'] * pins
    for i in range(balls):
        start, stop = [int(x) for x in
                       input("Start and stop pos: ").split()]
        for j in range(start - 1, stop):
            result[j] = '.'

    print(''.join(result))


def main():
    pins, balls = [int(i) for i in
                   input("Number of pins and balls: ").split()]

    knock(pins, balls)


if __name__ == '__main__':
    main()
