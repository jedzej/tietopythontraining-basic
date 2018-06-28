'''
In bowling, the player starts wtih 10 pins at the far end of a lane.
The object is to knock all the pins down. For this exercise,
the number of pins and balls will vary. Given the number
of pins N and then the number of balls K to be rolled,
followed by K pairs of numbers (one for each ball rolled),
determine which pins remain standing after all the balls have been rolled.
The balls are numbered from 1 to N (inclusive) for this situation.
The subsequent number pairs, one for each K represent the start to stop
(inclusive) positions of the pins that were knocked down with each role.
Print a sequence of N characters, where "I" represents a pin left standing
and "." represents a pin knocked down.
'''


def play_bowling():
    print("Enter pin and balls numbers separated by space [PIN BALLS]:")
    try:
        pin_number, balls_number = [int(s) for s in input("").split()]
    except ValueError:
        raise ValueError("Invalid pin and balls numbers")
    output = ['I'] * pin_number
    start_pin = 0
    end_pin = 0
    for i in range(balls_number):
        print(str(i + 1) + " ball thrown.")
        try:
            start_pin, end_pin = [int(s) for s in input(
                "Enter start to stop (inclusive) positions of the \
pins that were knocked down:").split()]
            for j in range(start_pin - 1, end_pin):
                output[j] = '.'
        except ValueError:
            raise ValueError("Invalid start and stop positions")
    print("I - represents pin left standing")
    print(". - represents a pin knocked down")
    print(''.join(output))


if __name__ == "__main__":
    try:
        play_bowling()
    except ValueError as e:
        print(e)
