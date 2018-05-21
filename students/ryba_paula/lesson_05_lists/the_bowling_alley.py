def knock_pins(pins, balls):
    result = pins * ['I']
    for i in range(balls):
        start, stop = [int(x) for x in input("Start and stop pos: ").split()]
        for j in range(start - 1, stop):
            result[j] = '.'

    print(''.join(result))


def main():
    a, b = [int(i) for i in input("Input pins and balls: ").split()]

    knock_pins(a, b)


if __name__ == '__main__':
    main()
