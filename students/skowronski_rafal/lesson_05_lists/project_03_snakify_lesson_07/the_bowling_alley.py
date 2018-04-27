def get_sequence_string(number_of_pins, *pairs):

    sequence = ['I' for i in range(number_of_pins)]
    for pair in pairs:
        begin, end = pair
        for i in range(begin - 1, end):
            sequence[i] = '.'

    return ''.join(sequence)


if __name__ == '__main__':
    number_of_pins = int(input('Enter number of pins: '))
    number_of_balls = int(input('Enter number of balls: '))
    print('Enter pairs: ')

    pairs = []
    for i in range(number_of_balls):
        pairs.append(tuple([int(i) for i in str(input()).split()]))

    print('Sequence string: {0}'
          .format(get_sequence_string(number_of_pins, *pairs)))
