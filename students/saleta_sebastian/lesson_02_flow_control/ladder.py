from __future__ import print_function


def print_ladder():
    last_step = int(input())

    for step_index in range(1, last_step + 1):
        for step in range(1, step_index + 1):
            print(step, sep='', end='')
        print()


if __name__ == '__main__':
    print_ladder()
