def print_sequence_reverse(sequence):
    if len(sequence) > 1:
        print_sequence_reverse(sequence[1:])
    print(sequence[0], end='')


def _is_int(char):
    try:
        int(char)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    sequence = [int(i)
                for i in
                input('Enter a sequence of integers ending with 0: ')
                if _is_int(i)]
    print_sequence_reverse(sequence)
