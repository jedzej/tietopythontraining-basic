# Solves problem 09 - Ladder


def _main():
    steps_number = int(input('Enter steps number (n): '))

    print(end='\n')
    for current_step in range(1, steps_number + 1):
        for i in range(1, current_step + 1):
            print(i, sep='', end='')
        print(end='\n')


if __name__ == '__main__':
    _main()
