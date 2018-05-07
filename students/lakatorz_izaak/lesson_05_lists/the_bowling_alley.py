# In bowling, the player starts wtih 10 pins at the far end of a lane. The
# object is to knock all the pins down. For this exercise, the number of
# pins and balls will vary. Given the number of pins N and then the number
# of balls K to be rolled, followed by K pairs of numbers (one for each ball
#  rolled), determine which pins remain standing after all the balls have
# been rolled. The balls are numbered from 1 to N (inclusive) for this
# situation. The subsequent number pairs, one for each K represent the start
#  to stop (inclusive) positions of the pins that were knocked down with
# each role. Print a sequence of N characters, where "I" represents a pin
# left standing and "." represents a pin knocked down.


def main():
    pins, balls = (int(a) for a in input("Enter pins and balls: ").split())
    pins_status = ['I'] * pins
    for i in range(balls):
        pins_start, pins_stop = (int(a) for a in input().split())
        if pins_start > pins_stop:
            pins_start, pins_stop = pins_stop, pins_start
        for j in range(pins_start-1, pins_stop):
            pins_status[j] = '.'

    print(''.join(pins_status))


if __name__ == "__main__":
    main()
